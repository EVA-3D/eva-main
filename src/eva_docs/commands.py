import asyncio
from base64 import b64decode
from pathlib import Path
from typing import Dict
from urllib.parse import quote

from rich.progress import Progress, BarColumn, TextColumn
from sqlmodel.sql.expression import select

from eva_docs.db import BOMTable as DBBOMTable, BOMItem as DBBOMItem, remove_bom_table
from onshape.client import Onshape
from onshape.schemas import BOMTable


ONSHAPE_SEMAPHORE = asyncio.Semaphore(10)



def get_progress_bar(task_description):
    text_column = TextColumn(f"{task_description}")
    bar_column = BarColumn(bar_width=None)
    return Progress(text_column, "•", bar_column, "•", "[progress.percentage]{task.percentage:>3.1f}%", expand=True)


def advance_progress_bar_callback(progress, task):
    def wrapped(future):
        progress.advance(task)
    return wrapped


async def run_semaphored(f, *args, **kwargs):
    async with ONSHAPE_SEMAPHORE:
        return await f(*args, **kwargs)


async def download_boms(onshape_credentials, cad_links: Dict[str, str]):
    progress = get_progress_bar("Generating Bills Of Materials")
    bom_tables = {}
    async with Onshape(**onshape_credentials) as onshape:
        with progress:
            tasks = {}
            progress_task = progress.add_task("", total=len(cad_links))
            for name, data in cad_links.items():
                if not "link" in data:
                    progress.console.print(f"Ignoring {name} due to missing link")
                    continue
                task = asyncio.create_task(
                    run_semaphored(
                        onshape.get_assembly_bom,
                        **Onshape.link(data["link"])
                    ),
                    name=name
                )
                task.add_done_callback(advance_progress_bar_callback(progress, progress_task))
                tasks[name] = task

            await asyncio.wait(tasks.values())

    for name, task in tasks.items():
        result = await task
        bom_tables[name] = BOMTable.parse_onshape(name, result)
        progress.console.print(f"BOM for {name} pulled")

    return bom_tables


def store_bom_tables(session, bom_tables: Dict[str, BOMTable]):
    progress = get_progress_bar("Storing Bills Of Materials")
    with progress:
        for bom_name, bom in progress.track(bom_tables.items()):
            remove_bom_table(session, bom_name)
            bom_table = DBBOMTable(name=bom_name)

            for item in bom.items:
                session.add(
                    DBBOMItem(
                        name=item.name,
                        bom_name=bom_name,
                        material=item.material.upper(),
                        quantity=item.quantity,
                        bom_table=bom_table,
                        source_did=item.source.did,
                        source_wvm_id=item.source.wvm_id,
                        source_wvm_type=item.source.wvm_type,
                        source_eid=item.source.eid,
                        source_part_id=item.source.part_id,
                        source_configuration=item.source.configuration,
                    )
                )
            session.commit()


async def download_images(onshape_credentials, cad_links: Dict[str, str], image_dir: Path):
    progress = get_progress_bar("Generating Images")
    async with Onshape(**onshape_credentials) as onshape:
        with progress:
            tasks = {}
            progress_task = progress.add_task("", total=len(cad_links))
            for name, data in cad_links.items():
                if not "link" in data:
                    progress.console.print(f"Ignoring {name} due to missing link")
                    continue
                task = asyncio.create_task(
                    run_semaphored(
                        onshape.get_shaded_view,
                        **Onshape.link(data["link"])
                    ),
                    name=name
                )
                task.add_done_callback(advance_progress_bar_callback(progress, progress_task))
                tasks[name] = task

            await asyncio.wait(tasks.values())

    for name, task in tasks.items():
        result = await task
        b64image = result["images"][0]
        image_path = (
            image_dir
            / f"{quote(name).lower()}.png"
        ).resolve()
        image_path.parent.mkdir(parents=True, exist_ok=True)
        with open(image_path, "wb") as image_file:
            image_file.write(b64decode(b64image))



def process_stl_file(bom_name: str, stls_dir, name: str, progress):
    def wrapped(future):
        try:
            result = future.result()
        except BaseException as exc:
            progress.console.print(f"[red] Error when pulling {bom_name}, file {name}: {exc}")
            return
        path_parts = bom_name.split(".")
        stl_path = Path(stls_dir, *path_parts, f"{name}.stl").resolve()
        stl_path.parent.mkdir(parents=True, exist_ok=True)
        with open(stl_path, "wb") as stl_file:
            stl_file.write(result)
    return wrapped



async def download_stls(onshape_credentials, session, stls_dir: Path):
    progress = get_progress_bar("Pulling STLs")
    items = session.exec(select(DBBOMItem).where(DBBOMItem.material == "PETG")).all()
    async with Onshape(**onshape_credentials) as onshape:
        with progress:
            progress_task = progress.add_task("", total=len(items))
            tasks = []
            for item in items:
                if item.is_printable:
                    task = asyncio.create_task(
                        run_semaphored(
                            onshape.export_part,
                            did=item.source_did, 
                            wvm_id=item.source_wvm_id, 
                            wvm_type=item.source_wvm_type, 
                            eid=item.source_eid, 
                            part_id=item.source_part_id, 
                            configuration=item.source_configuration,
                        ),
                        name=item.name
                    )
                    task.add_done_callback(advance_progress_bar_callback(progress, progress_task))
                    task.add_done_callback(process_stl_file(item.bom_name, stls_dir, item.name, progress))
                    tasks.append(task)

            await asyncio.gather(*tasks)
