---
title: Bowden
uid: EVA / Bowden
type: drive
badges:
    - Official
contributors: 
    - pkucmus
repo_url: https://github.com/EVA-3D/eva-bowden
cad_url: https://cad.onshape.com/documents/1765b04fac582f6c1c470bd3/w/1cc31596374d6ce51cd23fa9/e/97f38bca98acd8d24f463d78
satisfies:
    - drive
boms:
    - id: Bowden.MGN12
      source: ./bom/Bowden.MGN12.csv
      namespace: drives
    - id: Bowden.MGN15
      source: ./bom/Bowden.MGN15.csv
      namespace: drives
---
# Bowden

![preview](assets/Bowden.png)

As I don't expect this one to be used much on CoreXY machines it will come handy for some V-casts or cantilever printers. EVA 2 / Bowden is built with the base parts of EVA that are later on "remixed" to achieve different drive types.

!!! info "Universal EVA Front"

    This drive uses the universal face, which means it's comatible with all hotends you can find in the Hotends section.

??? info "PC4-M6"

    Mosquito, Dragon and V6 (clones) that do not have the PTFE grabbing collar do need a PC4-M6 "pneumatic fitting" on the hot end side to grab the bowden tube. The parts do not have threads but the hole size allows for self-tapping.

    ![](assets/PC4-M6.png)

    Make sure to get the connector that allows the bowden to go through it:

    ![](assets/PC4-M6_through.png)

### Bill of materials


=== "MGN12"

    <add-bom-button name="{{ meta.uid }} (MGN12)">
        {{ get_bom("Bowden.MGN12").json()|b64encode }}
    </add-bom-button>
    
    {{ get_bom("Bowden.MGN12").md_table(4) }}


=== "MGN15"

    <add-bom-button name="{{ meta.uid }} (MGN15)">
        {{ get_bom("Bowden.MGN15").json()|b64encode }}
    </add-bom-button>
    
    {{ get_bom("Bowden.MGN15").md_table(4) }}


### Links

{{ download_button }}
{{ cad_link }}
