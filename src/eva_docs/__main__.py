import asyncio
from pathlib import Path
import shutil

import click
from mkdocs.__main__ import cli as mkdocs_cli
from mkdocs import config

from eva_docs.commands import (
    download_boms,
    download_images,
    download_stls,
    store_bom_tables,
)
from eva_docs.db import create_db_and_tables, db_session
from onshape.client import Onshape


@click.group()
@click.pass_context
# @click.option(
#     "--onshape-access-key", envvar="ONSHAPE_ACCESS", prompt=True, hide_input=True
# )
# @click.option(
#     "--onshape-secret-key", envvar="ONSHAPE_SECRET", prompt=True, hide_input=True
# )
# def cli(ctx, onshape_access_key, onshape_secret_key):
def cli(ctx):
    mkdocs_config = config.load_config(site_dir="/tmp/eva-3d-unpack")
    ctx.obj = {}
    ctx.obj["mkdocs_config"] = mkdocs_config
    ctx.obj["project_dir"] = Path(mkdocs_config["docs_dir"]).parent.resolve()
    ctx.obj["eva_docs"] = mkdocs_config["plugins"]["eva-docs-plugin"]
    ctx.obj["onshape_credentials"] = {
        "access_key": "M48ljFC1VUmEv986xjM2vHUK",
        "secret_key": "4AT7d2XqHOAJLmAaiSeYeiug3XAQqyLy0Ksp7GxDJ7y48F1t",
    }
    create_db_and_tables()


@cli.command()
@click.pass_context
def run_all(ctx):
    # ctx.forward(get_boms)
    # ctx.forward(get_images)
    ctx.forward(get_stls)


@cli.command()
@click.pass_context
def get_boms(ctx):
    bom_tables = asyncio.run(
        download_boms(
            ctx.obj["onshape_credentials"], ctx.obj["eva_docs"].config["assemblies"]
        )
    )
    with db_session() as session:
        store_bom_tables(session=session, bom_tables=bom_tables)


@cli.command()
@click.pass_context
def get_images(ctx):
    image_dir = (Path("docs") / "onshape_assets").resolve()
    shutil.rmtree(image_dir, ignore_errors=True)
    asyncio.run(
        download_images(
            ctx.obj["onshape_credentials"],
            ctx.obj["eva_docs"].config["assemblies"],
            image_dir=image_dir,
        )
    )


@cli.command()
@click.pass_context
def get_stls(ctx):
    stls_dir = (Path("docs") / "stls").resolve()
    shutil.rmtree(stls_dir, ignore_errors=True)
    with db_session() as session:
        asyncio.run(
            download_stls(
                onshape_credentials=ctx.obj["onshape_credentials"],
                session=session,
                stls_dir=stls_dir,
            )
        )
