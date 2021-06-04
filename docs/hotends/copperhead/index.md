---
title: Copperhead
uid: EVA / Copperhead
type: hotend
badges:
    - Official
contributors: 
    - pkucmus
# repo_url: https://github.com/EVA-3D/eva-bmg
cad_url: https://cad.onshape.com/documents/980a8bb4514542eeb90c5c21/w/fd1e2bf7da865e46d00cc945/e/7a40b6f26ab1209ef8f4cf56
satisfies:
    - hotend
boms:
    - id: Copperhead
      source: ./bom/Copperhead.csv
      namespace: hotends
---

# Copperhead

![preview](assets/Copperhead.png)

## Bill of materials


<add-bom-button name="{{ meta.uid }}">
    {{ get_bom("Copperhead").json()|b64encode }}
</add-bom-button>

{{ get_bom("Copperhead").md_table(4) }}

## Links

{{ download_button }}
{{ cad_link }}
