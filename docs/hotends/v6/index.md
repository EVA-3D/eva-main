---
title: E3D V6
uid: EVA / V6
type: hotend
badges:
    - Official
contributors: 
    - pkucmus
# repo_url: https://github.com/EVA-3D/eva-bmg
cad_url: https://cad.onshape.com/documents/1765b04fac582f6c1c470bd3/w/1cc31596374d6ce51cd23fa9/e/e2fc56d355d28a162332ce38
satisfies:
    - hotend
boms:
    - id: V6
      source: ./bom/V6.csv
      namespace: hotends
---

# E3D V6

![preview](assets/V6.png)

## Bill of materials


<add-bom-button name="{{ meta.uid }}">
    {{ get_bom("V6").json()|b64encode }}
</add-bom-button>

{{ get_bom("V6").md_table(4) }}

## Links

{{ download_button }}
{{ cad_link }}
