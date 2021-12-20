---
title: BMG
icon: material/cog
uid: EVA / BMG
type: drive
spec: 2.4.0
badges:
    - official
contributors: 
    - pkucmus
cad_url: https://cad.onshape.com/documents/8669b75b86d079defa27c647/w/c7d4d8da0ad3b529c7c85328/e/e23dd2f45ad2e8d07def9191
satisfies:
    - drive
usage: 0.213
---

{% extends 'drives.md' %}

{% block description %}

Read about the BMG® Extruder here: https://www.bondtech.se/product/bmg-extruder/

{{ super() }}

(Survey result is shared with [BMG-M](/drives/bmg-m/))

!!! info "Universal EVA Front"

    This drive uses the universal face, which means it's compatible with all hotends you can find in the Hotends section.

{% endblock description %}
