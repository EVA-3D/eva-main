# EVA 2 / Project Template

See `help.md` for some shortcuts. Remember to remove of hide `help.md` before deployment.

The directory tree of a EVA 2 submodule can look like this:

```
.
├── assets
├── bom
├── downloads
├── stls
├── help.md
└── index.md
```

## Assets

The `assets` direcotry should hold graphics, animations, etc

## BOM

The `bom` directory should hold a Onshape compatible BOM CSV containing 4 columns (case and order sensitive), comma separated, `"` as the string quotation sign, e.g.:

```
Item No.,Quantity,Name,Material
1,1,bottom_mgn12_short_duct,PETG
```

If a bom file is made like that then the `{{ bom("drives/bmg/bom/e3d.csv", 4) }}` macro can be used in the template. The bom file is also used with the `eva-3d unpack-stls` command used by the main documentation project. More on that in the `downloads` section.
Printable parts need to have their material assigned as `PETG` to be properly exported.

## Downloads

The `downloads` directory is supposed to contain a zip package with every printable part a project will have, the bom is used to list all printable parts and extract those by filename to be later referenced by the `bom` macro.

## STLs

This directory is automatically populated by the process described above but if one will find the zip generation method to complex - there is still the possibility to place the STL files here manually. It's highly recommended not to :)

## Help.md

Is just a list of features of [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), remove the file before releasing.

# FAQ

1. Pages other than `index.md` do not render, how to fix that?

That behavior is there by design. If you want to add another page you need to edit the `.pages` file.
