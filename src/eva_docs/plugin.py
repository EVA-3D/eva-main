import asyncio
from pathlib import Path
import shutil
from typing import Optional

import aiofiles
import yaml
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
from mkdocs.structure.files import get_files

from eva_docs import db

# ORDER = {
#     "core": 0,
#     "hotend": 1,
#     "drive": 2,
#     "cooling_inlet": 3,
#     "probes": 4,
# }

class EVAPlugin(BasePlugin):

    config_scheme = (
        ("version", config_options.Type(str)),
        ("assemblies", config_options.Type(dict)),
        ("pages", config_options.Type(dict)),
        ("stls_dir", config_options.Type(str)),
        ("onshape_assets_dir", config_options.Type(str)),
    )

    def on_config(self, config):
        self.context = {}
        self.docs_config = config
        self.env = config["theme"].get_env()
        self.env.filters["md_table"] = self.md_table
        self.env.filters["yes_no"] = self.yes_no
        self.env.filters["to_yaml"] = self.to_yaml

        self.project_dir = Path(config["docs_dir"]).parent.resolve()
        self.include_dir = self.project_dir / "include"

        self.assemblies_order = {}
        for index, key in enumerate(self.config["assemblies"].keys()):
            key_parts = key.split(".")
            if len(key_parts) > 2:
                self.assemblies_order.setdefault(key_parts[1], index)

    # def on_build_error(self, error):
    #     import ipdb; ipdb.post_mortem()

    def _get_markdown_context(self, page, config):
        return {
            "meta": page.meta,
            "get_bom": self.get_bom,
            "get_cad_link": self.get_cad_link,
            "assembly_data": self.assembly_data,
            "button": self.button,
            **self.context,
        }

    def render_markdown(self, markdown, page, config):
        md_template = self.env.from_string(markdown)
        return md_template.render(**self._get_markdown_context(page, config))

    def file_sort(self, file_):
        path_parts = file_.src_path.split("/")
        if len(path_parts) > 2:
            return self.assemblies_order.get(path_parts[1], 99)
        return 0

    def on_files(self, files, config):
        component_files = get_files({
            "docs_dir": self.include_dir,
            "site_dir": config["site_dir"],
            "use_directory_urls": config["use_directory_urls"],
        })
        for component_file in sorted(component_files._files, key=self.file_sort):
            files.append(component_file)

        return files

    async def make_template_cache(self, assemblies):
        template_cache = {}
        for name, data in assemblies.items():
            template_path = self.project_dir / data.get(
                "template_path", "overrides/component_template.md"
            )
            if not template_path in template_cache:
                async with aiofiles.open(template_path, "r") as template_file:
                    template = self.env.from_string(await template_file.read())
                    template_cache[template_path] = template
            else:
                template = template_cache[template_path]

        return template_cache

    async def gen_page(self, template_cache, dest_dir, name, data):
        path_parts = name.split(".")
        title = data.get("title", path_parts[-1])

        path = Path(dest_dir, *path_parts[:-1], f"{path_parts[-1]}.md")
        meta = {
            "title": title,
            "eva": {
                "name": name,
            },
        }
        try:
            meta["eva"]["mounting"] = path_parts[0]
        except IndexError:
            pass

        try:
            meta["eva"]["category"] = path_parts[1]
        except IndexError:
            pass

        try:
            meta["eva"]["component"] = path_parts[2]
        except IndexError:
            pass

        if icon := data.get("icon"):
            meta["icon"] = icon

        template_path = self.project_dir / data.get(
            "template_path", "overrides/component_template.md"
        )
        if not template_path in template_cache:
            async with aiofiles.open(template_path, "r") as template_file:
                template = self.env.from_string(await template_file.read())
        else:
            template = template_cache[template_path]

        path.parent.mkdir(parents=True, exist_ok=True)

        async with aiofiles.open(path, "w") as dest_file:
            await dest_file.write(
                template.render(
                    {
                        "title": title,
                        "meta": meta,
                        "description": data.get("description", "") or "",
                    }
                )
            )

    async def gen_pages(self, dest_dir, assemblies):
        template_cache = await self.make_template_cache(assemblies)
        coros = [self.gen_page(template_cache, dest_dir, name, data) for name, data in assemblies.items()]
        await asyncio.gather(*coros)

    def on_pre_build(self, config):
        dest_dir = self.include_dir
        shutil.rmtree(dest_dir, ignore_errors=True)

        asyncio.run(self.gen_pages(dest_dir, self.config["assemblies"]))

    def on_page_markdown(self, markdown, page, config, files):
        return self.render_markdown(markdown, page, config)

    def get_bom(self, assembly_id):
        with db.db_session() as session:
            return db.get_bom_table(session=session, bom_table_name=assembly_id)

    def assembly_data(self, assembly_id):
        return self.config["assemblies"][assembly_id]

    def get_cad_link(self, assembly_id):
        return self.button(
            "CAD",
            self.assembly_data(assembly_id)["link"],
            ":fontawesome-solid-file-import:",
            True,
        )

    @staticmethod
    def yes_no(value: bool):
        return "yes" if value else "no"

    @staticmethod
    def to_yaml(value: bool):
        return yaml.safe_dump(value)

    def md_table(self, bom_table: db.BOMTable, indent: int = 0):
        if not isinstance(bom_table, db.BOMTable):
            return ""
        indent_str = " " * indent
        rows = []
        for index, item in enumerate(bom_table.items):
            if index == 0:
                rows.append(f"| Item | Quantity | Name | Printable |")
                rows.append(
                    "{}| {} |".format(
                        indent_str,
                        " | ".join(["-" * len(str(col)) for col in range(4)]),
                    )
                )
            if item.is_printable:
                url_parts = [self.config['stls_dir']]
                url_parts.extend(item.bom_name.split("."))
                url_parts.append(f"{item.name}.stl")
                url = "/".join(url_parts)
                rows.append(
                    f"{indent_str}| {index + 1} | {item.quantity} | [{item.name}](/{url}) | {self.yes_no(item.is_printable)} |"
                )
            else:
                rows.append(
                    f"{indent_str}| {index + 1} | {item.quantity} | {item.name} | {self.yes_no(item.is_printable)} |"
                )
        return "\n".join(rows)

    def button(
        self,
        title: str,
        href: str,
        icon: Optional[str] = None,
        open_in_new_tab: bool = False,
    ):
        target = ""
        if open_in_new_tab:
            target = "target='_blank'"

        if icon:
            icon = f"{icon} "
        else:
            icon = ""

        return f"[{icon}{title}]({href}){{: .md-button .md-button--primary {target}}}"
