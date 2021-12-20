---
title: Bowden
icon: material/cog
uid: EVA / Bowden
type: drive
spec: 2.4.0
badges:
    - official
contributors: 
    - pkucmus
cad_url: https://cad.onshape.com/documents/1765b04fac582f6c1c470bd3/w/1cc31596374d6ce51cd23fa9/e/f36b4d773104fcd6926a6641
satisfies:
    - drive
usage: 0.0
---

{% extends 'drives.md' %}

{% block description %}

As I don't expect this one to be used much on CoreXY machines it will come handy for some V-casts or cantilever printers. EVA 2 / Bowden is built with the base parts of EVA that are later on "remixed" to achieve different drive types.

{{ super() }}

??? info "PC4-M6"

    Mosquito, Dragon and V6 (clones) that do not have the PTFE grabbing collar do need a PC4-M6 "pneumatic fitting" on the hot end side to grab the bowden tube. The parts do not have threads but the hole size allows for self-tapping.

    ![](assets/PC4-M6.png)

    Make sure to get the connector that allows the bowden to go through it:

    ![](assets/PC4-M6_through.png)

!!! info "Universal EVA Front"

    This drive uses the universal face, which means it's compatible with all hotends you can find in the Hotends section.

{% endblock description %}
