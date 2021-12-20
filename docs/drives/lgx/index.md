---
title: LGX
icon: material/cog
uid: EVA / LGX
type: drive
spec: 2.4.0
badges:
    - official
contributors: 
    - pkucmus
cad_url: https://cad.onshape.com/documents/d2a2f19b34851a8570487add/w/1ff9bb9662c715a9cdc3d984/e/f74cb56cf915933a84ff4023
satisfies:
    - drive
usage: 0.341
---

{% extends 'drives.md' %}

{% block description %}

Read about the LGX® Large Gears eXtruder here: https://www.bondtech.se/product/lgx-large-gears-extruder/

{{ super() }}

!!! info "Universal EVA Front"

    This drive uses the universal face, which means it's compatible with all hotends you can find in the Hotends section.

??? Question "What about LGX For Flexibles Set?"

    The decision was made, I don't want the front heavy - so called compact - extruders on EVA. Those do not fit EVA.

{% endblock description %}
