---
title: Mosquito
uid: EVA / Mosquito
type: hotend
badges:
    - Official
contributors: 
    - pkucmus
# repo_url: https://github.com/EVA-3D/eva-bmg
cad_url: https://cad.onshape.com/documents/1765b04fac582f6c1c470bd3/w/1cc31596374d6ce51cd23fa9/e/2a1118238518a84a214f8af2
satisfies:
    - hotend
boms:
    - id: Mosquito
      source: ./bom/Mosquito.csv
      namespace: hotends
---

# Mosquito

![preview](assets/Mosquito.png)

## Bill of materials


<add-bom-button name="{{ meta.uid }}">
    {{ get_bom("Mosquito").json()|b64encode }}
</add-bom-button>

{{ get_bom("Mosquito").md_table(4) }}

## Links

{{ download_button }}
{{ cad_link }}
