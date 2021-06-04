---
title: Dragon
uid: EVA / Dragon
type: hotend
badges:
    - Official
contributors: 
    - pkucmus
# repo_url: https://github.com/EVA-3D/eva-bmg
cad_url: https://cad.onshape.com/documents/1765b04fac582f6c1c470bd3/w/1cc31596374d6ce51cd23fa9/e/7469266a17bbe063b78e3d31
satisfies:
    - hotend
boms:
    - id: Dragon
      source: ./bom/Dragon.csv
      namespace: hotends
---

# Dragon

![preview](assets/Dragon.png)

## Bill of materials


<add-bom-button name="{{ meta.uid }}">
    {{ get_bom("Dragon").json()|b64encode }}
</add-bom-button>

{{ get_bom("Dragon").md_table(4) }}

## Links

{{ download_button }}
{{ cad_link }}
