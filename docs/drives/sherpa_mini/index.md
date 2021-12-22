---
title: Sherpa Mini
icon: material/star-cog
uid: EVA / Sherpa Mini
type: drive
spec: 2.4.0
badges:
    - official
contributors: 
    - pkucmus
cad_url: https://cad.onshape.com/documents/faf4a53a25c3b788e478203f/w/13643fbd02f4c673d9ddcb4f/e/b847abd8bc1a14592e0f40ea
satisfies:
    - drive
usage: 0.161
---

{% extends 'drives.md' %}

{% block description %}

Sherpa Mini extruder is an extruder Developed by Annex Engineering, you can find more about it [:material-github: here](https://github.com/Annex-Engineering/Sherpa_Mini-Extruder).

Sherpa Mini works best with EVA with the ["K" part](https://github.com/Annex-Engineering/Sherpa_Mini-Extruder/blob/master/STLs/FDM_STLs/optional_parts/%5Ba%5D_housing_front_k_x1_rev5.STL). Also the mounting from the back might be "controversial" but that was the most optimal solution I could figure out to save X space (having IDEX in mind).

{{ super() }}

!!! info "Universal EVA Front"

    This drive uses the universal face, which means it's compatible with all hotends you can find in the Hotends section.

{% endblock description %}
