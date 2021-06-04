---
title: X Endstop
badges:
    - Official
uid: EVA / Addons / Endstops
type: addon
contributors: 
    - pkucmus
repo_url: https://github.com/EVA-3D/addon-endstops
cad_url: https://cad.onshape.com/documents/d24027dd78e7164add26b5f5/w/0615251dcae8664926ca1aa2/e/e01d9ebd9e9d0542d74812ce
satisfies:
    - endstop
boms:
    - id: BOM_Endstops.sensorless.MGN12
      source: ./bom/BOM_Endstops.sensorless.MGN12.csv
      namespace: x_endstops
    - id: BOM_Endstops.sensorless.MGN15
      source: ./bom/BOM_Endstops.sensorless.MGN15.csv
      namespace: x_endstops
    - id: BOM_Endstops.angled.MGN12
      source: ./bom/BOM_Endstops.angled.MGN12.csv
      namespace: x_endstops
    - id: BOM_Endstops.angled.MGN15
      source: ./bom/BOM_Endstops.angled.MGN15.csv
      namespace: x_endstops
    - id: BOM_Endstops.openbuilds.MGN12
      source: ./bom/BOM_Endstops.openbuilds.MGN12.csv
      namespace: x_endstops
    - id: BOM_Endstops.openbuilds.MGN15
      source: ./bom/BOM_Endstops.openbuilds.MGN15.csv
      namespace: x_endstops
---

![](assets/__ALL__.png)

## Standard

All EVA carriages have endstop slots in their `top` parts. Those are different depending on the MGN carriage but **consistent** in their spec. This is to make it easy to design different endstop mounts.

By default 3 types are provided.

=== "Sensorless"

    === "MGN12"

        <add-bom-button name="{{ meta.uid }} (sensorless_MGN12)">
            {{ get_bom("BOM_Endstops.sensorless.MGN12").json()|b64encode }}
        </add-bom-button>
        
        {{ get_bom("BOM_Endstops.sensorless.MGN12").md_table(8) }}

    === "MGN15"

        <add-bom-button name="{{ meta.uid }} (sensorless_MGN15)">
            {{ get_bom("BOM_Endstops.sensorless.MGN15").json()|b64encode }}
        </add-bom-button>
        
        {{ get_bom("BOM_Endstops.sensorless.MGN15").md_table(8) }}

=== "Angled Endstop"

    === "MGN12"

        <add-bom-button name="{{ meta.uid }} (angled_MGN12)">
            {{ get_bom("BOM_Endstops.angled.MGN12").json()|b64encode }}
        </add-bom-button>
        
        {{ get_bom("BOM_Endstops.angled.MGN12").md_table(8) }}

    === "MGN15"

        <add-bom-button name="{{ meta.uid }} (angled_MGN15)">
            {{ get_bom("BOM_Endstops.angled.MGN15").json()|b64encode }}
        </add-bom-button>
        
        {{ get_bom("BOM_Endstops.angled.MGN15").md_table(8) }}

=== "Openbuilds"

    === "MGN12"

        <add-bom-button name="{{ meta.uid }} (openbuilds_MGN12)">
            {{ get_bom("BOM_Endstops.openbuilds.MGN12").json()|b64encode }}
        </add-bom-button>
        
        {{ get_bom("BOM_Endstops.openbuilds.MGN12").md_table(8) }}

    === "MGN15"

        <add-bom-button name="{{ meta.uid }} (openbuilds_MGN15)">
            {{ get_bom("BOM_Endstops.openbuilds.MGN15").json()|b64encode }}
        </add-bom-button>
        
        {{ get_bom("BOM_Endstops.openbuilds.MGN15").md_table(8) }}


## Links

{{ download_button }}
{{ cad_link }}
