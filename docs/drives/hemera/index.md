---
title: Hemera
icon: material/cog-pause
uid: EVA / Hemera
type: drive
spec: 2.3.0
badges:
    - official
contributors: 
    - pkucmus
cad_url: https://cad.onshape.com/documents/371450c83b99fdd5844f4b0c/w/6283a21a1cfe91323a72f862/e/1fc412a1de950c20053d2aaa
satisfies:
    - drive
usage: 0.052
---

{% extends 'drives.md' %}

{% block header %}
??? warning "EVA / Hemera is still on EVA 2.3.0"

    Due to the reasons described bellow I had to omit upgrading Hemera to the newest spec, the main issue is the need for driving the main 35-40mm screws from the back. Sorry.

??? danger "Possible deprecation warning"

    EVA / Hemera takes 50% of the work while being used by only 5.2% of the users, it's not fully to spec and in general Hemera is not a great fit for EVA. I don't want to be slowed down by it and my goal is to get rid of it from the platform.
    
    This means that it will stop receiving upgrades but will forever be available in the 2.3.0 version in it's [submodule repository](https://github.com/EVA-3D/eva-hemera).

{% endblock header %}

{% block description %}

E3D Hemera is an example of the front heavy EVAs (Aero was the same). The motor is huge and the whole extruder takes a lot of space so make sure to understand that the **full print volume may not be accessible** when using this EVA variant.

??? question "Why not bellow the rail?"

    I tried that on Aero - it did not work and was rendering it out of spec even more.

Hemera's motor needs to be put on quite early in the assembly process, remember to grab the right belt before putting it on.

{{ super() }}

{% endblock description %}
