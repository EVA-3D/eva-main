---
title: BMG
uid: EVA / BMG
type: drive
badges:
    - Official
contributors: 
    - pkucmus
repo_url: https://github.com/EVA-3D/eva-bmg
cad_url: https://cad.onshape.com/documents/8669b75b86d079defa27c647/w/c7d4d8da0ad3b529c7c85328/e/d9184d31fd3592039cc4b5f8
satisfies:
    - drive
boms:
    - id: BMG.MGN12
      source: ./bom/BMG.MGN12.csv
      namespace: drives
    - id: BMG.MGN15
      source: ./bom/BMG.MGN15.csv
      namespace: drives
---

# BMG

![preview](assets/BMG.png)

This one is one of my favourites, like the Titan one the filament path is not super short but that's an exchange for the modularity EVA provides, also it does not seem to make much difference. EVA 2 / BMG is compatible with both the standard BMG and BMG-M for all hotend options.  
I'm personally using this EVA drive variant.

!!! info "Universal EVA Front"

    This drive uses the universal face, which means it's comatible with all hotends you can find in the Hotends section.

??? tip "BMG-M users - please read"

    Since EVA 2.1.0 the direct interface between the hotend and the extruder is removed, that means there's nothing holding the PTFE tube in place on top. To alleviate that a `bmg-m_pfte_adapter` part was made which is screwed into the BMG-M that will hold the tube in place.

    This assembly requires two `M2.5 10mm screws` and the [`bmg-m_pfte_adapter`](extra_stls/bmg-m_pfte_adapter.stl) part.

    ![](assets/bmg-m.png)

### Bill of materials


=== "MGN12"

    <add-bom-button name="{{ meta.uid }} (MGN12)">
        {{ get_bom("BMG.MGN12").json()|b64encode }}
    </add-bom-button>
    
    {{ get_bom("BMG.MGN12").md_table(4) }}


=== "MGN15"

    <add-bom-button name="{{ meta.uid }} (MGN15)">
        {{ get_bom("BMG.MGN15").json()|b64encode }}
    </add-bom-button>
    
    {{ get_bom("BMG.MGN15").md_table(4) }}


#### PTFE Tube lenghts

| Hotend | Length |
| ------ | ------ |
| Mosquito | 45.5 mm |
| E3D V6 | 62 mm |
| Dragon | 47 mm |
| Copperhead | 61 mm |

### Links

{{ download_button }}
{{ cad_link }}

