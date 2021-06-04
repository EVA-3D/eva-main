---
title: Bed Probing
uid: EVA / Addons / Probes
type: addon
badges:
    - Official
contributors: 
    - pkucmus
repo_url: https://github.com/EVA-3D/addon-probes
cad_url: https://cad.onshape.com/documents/94cafeab52e3dfa0a28bae89/w/99794094315556b24b5664ec/e/e50692a479f24cc5bf03727a
satisfies:
    - bed_probe
boms:
    - id: inductive_8mm
      source: ./bom/inductive_8mm.csv
      namespace: probes
    - id: inductive_12mm
      source: ./bom/inductive_12mm.csv
      namespace: probes
    - id: inductive_18mm
      source: ./bom/inductive_18mm.csv
      namespace: probes
    - id: bltouch
      source: ./bom/bltouch.csv
      namespace: probes
    - id: bltouch_alt
      source: ./bom/bltouch_alt.csv
      namespace: probes
---

# Bed Probing

![preview](assets/__ALL__.png)

This EVA Addon is supposed to contain different mounting solutions for different bed probe options. In some cases it might make more sense to mirror the mount in the slicer to move the probe to the right side of the carriage.

## Offsets

=== "Inductive Probe"
    === "8mm"

        <img src="assets/LJ8_probe_mount.png" width="300"/>

        - Hemera: `X31.48`, `Y-41.69`
        - Aero: `X-50.35`, `Y8` or `X-14`, `Y-44.9`
        - Others: `X-27.8`, `Y-12`

        <add-bom-button name="{{ meta.uid }} (LJ8)">
            {{ get_bom("inductive_8mm").json()|b64encode }}
        </add-bom-button>
        
        {{ get_bom("inductive_8mm").md_table(8) }}

    === "12mm"

        <img src="assets/LJ12_probe_mount.png" width="300"/>

        - Hemera: `X32.98`, `Y-43.69`
        - Aero: `X-52.35`, `Y6.5` or `X-12.5`, `Y-46.9`
        - Others: `X-29.8`, `Y-13.5`

        <add-bom-button name="{{ meta.uid }} (LJ12)">
            {{ get_bom("inductive_12mm").json()|b64encode }}
        </add-bom-button>
        
        {{ get_bom("inductive_12mm").md_table(8) }}

    === "18mm"

        <img src="assets/LJ18_probe_mount.png" width="300"/>

        - Hemera: `X36.98`, `Y-46.69`
        - Aero: `X-55.35`, `Y2.5` or `X-8.5`, `Y-49.9`
        - Others: `X-32.8`, `Y-17.5`

        <add-bom-button name="{{ meta.uid }} (LJ18)">
            {{ get_bom("inductive_18mm").json()|b64encode }}
        </add-bom-button>
        
        {{ get_bom("inductive_18mm").md_table(8) }}

=== "BLTouch"
    === "Standard"

        <img src="assets/bl_touch_mount.png" width="300"/>

        - Hemera: `X32.5`, `Y-42`
        - Aero: `X-50.55`, `Y7` or `X-13`, `Y-45.1`
        - Others: `X-28`, `Y-13`

        <add-bom-button name="{{ meta.uid }} (BL)">
            {{ get_bom("bltouch").json()|b64encode }}
        </add-bom-button>
        
        {{ get_bom("bltouch").md_table(8) }}

    === "Alternative"

        <img src="assets/bl_touch_mount_alt.png" width="300"/>

        - Hemera: `X24.5`, `Y-46.84`
        - Aero: `X-58`, `Y15` or `X-21`, `Y-50.6`
        - Others: `X-33.48`, `Y-5`

        <add-bom-button name="{{ meta.uid }} (BL-alt)">
            {{ get_bom("bltouch_alt").json()|b64encode }}
        </add-bom-button>
        
        {{ get_bom("bltouch_alt").md_table(8) }}


## Links

{{ download_button }}
{{ cad_link }}
