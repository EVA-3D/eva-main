---
title: BMG-M
icon: material/cog
uid: EVA / BMG-M
type: drive
spec: 2.4.0
badges:
    - official
contributors: 
    - pkucmus
cad_url: https://cad.onshape.com/documents/8669b75b86d079defa27c647/w/c7d4d8da0ad3b529c7c85328/e/a884b888a3f9095b1916cded
satisfies:
    - drive
usage: 0.213
---

{% extends 'drives.md' %}

{% block description %}

Read about the BMG® Extruder here: https://www.bondtech.se/product/bmg-extruder/

{{ super() }}

(Survey result is shared with [BMG](/drives/bmg/))

!!! info "Universal EVA Front"

    This drive uses the universal face, which means it's compatible with all hotends you can find in the Hotends section.

{% endblock description %}
