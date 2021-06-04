---
title: Orbiter
uid: EVA / Orbiter
type: drive
badges:
    - Official
contributors: 
    - pkucmus
repo_url: https://github.com/EVA-3D/eva-orbiter
cad_url: https://cad.onshape.com/documents/bb8303124bc8370b6d1924bc/w/8276a22c579374e8b02e9b96/e/7e46b442be945fb22f5c7c28
satisfies:
    - drive
boms:
    - id: Orbiter.MGN12
      source: ./bom/Orbiter.MGN12.csv
      namespace: drives
    - id: Orbiter.MGN15
      source: ./bom/Orbiter.MGN15.csv
      namespace: drives
---
# Orbiter

![preview](assets/Orbiter.png)

EVA 2 now supports [The Orbiter](https://www.thingiverse.com/thing:4725897){target=_blank} created by Robert Lorincz. 

Since EVA 2.2.1 Orbiter 1.5 is the only supported version of the Orbiter.

!!! info "Universal EVA Front"

    This drive uses the universal face, which means it's comatible with all hotends you can find in the Hotends section.

??? info "Orbiter 1.0 users"

    Old parts supporting the old Orbiter can be found in git history on tag [2.2.0](https://github.com/EVA-3D/eva-orbiter/tree/2.2.0/stls){target=_blank}

### BOM


=== "MGN12"

    <add-bom-button name="{{ meta.uid }} (MGN12)">
        {{ get_bom("Orbiter.MGN12").json()|b64encode }}
    </add-bom-button>
    
    {{ get_bom("Orbiter.MGN12").md_table(4) }}


=== "MGN15"

    <add-bom-button name="{{ meta.uid }} (MGN15)">
        {{ get_bom("Orbiter.MGN15").json()|b64encode }}
    </add-bom-button>
    
    {{ get_bom("Orbiter.MGN15").md_table(4) }}

#### PTFE Tube lenghts

| Hotend | Length |
| ------ | ------ |
| Mosquito | 60.3 mm |
| E3D V6 | 43.8 mm |
| Dragon | 45.3 mm |
| Copperhead | 59.3 mm |

### Links

{{ download_button }}
{{ cad_link }}
