---
title: Inductive
icon: material/cog
uid: EVA / Addons / Inductive
type: addon
spec: 2.4.0
badges:
    - Official
contributors: 
    - pkucmus
cad_url: https://cad.onshape.com/documents/94cafeab52e3dfa0a28bae89/w/99794094315556b24b5664ec/e/add7606d94bef518a043ed5f
satisfies:
    - bed_probe
---

{% extends 'addons.md' %}

{% block description %}
{{super()}}

The BOM will define a sum of the part for all variants, you only need one printed part and one probe.
{% endblock description %}
