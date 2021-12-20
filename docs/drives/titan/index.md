---
title: Titan
icon: material/cog-pause
uid: EVA / Titan
type: drive
spec: 2.4.0
badges:
    - official
contributors: 
    - pkucmus
cad_url: https://cad.onshape.com/documents/bb6db4fbcd7c5ec5350427f0/w/8da16df4512074fe4659384c/e/d0fc464a4453631a662f183c
satisfies:
    - drive
usage: 0.013
---

{% extends 'drives.md' %}

{% block header %}
??? danger "Deprecation warning"

    Sadly, but due to the lack of interest for EVA / Titan I will be deprecating it. Titan served us well, especially in the early days as an alternative for the lousy extruders printers came with.

    Deprectaion means that this is the last release this variant got an update, next time it will be marked as *obsolete*. This means that it will stop receiving upgrades but will forever be available in the 2.4.0 version in it's [submodule repository](https://github.com/EVA-3D/eva-titan).
{% endblock header %}

{% block description %}

EVA / Titan is the oldest and ~~in my opinion one of the best variants~~ the one quite closest to my heart as it was the original and only extruder option for the first [Easy-Mod](https://eva-3d.github.io/easy-mod/) - later was moved to a separate project which EVA become :smile:  
Since EVA 2.0.0 it does not require a unique `front` part, just a `top` (like BMG) which makes it not only easier to assemble but also to maintain. One can opt to use the `press fit` part if is lacking a groove mount adapter.  
There is a PTFE tube going from the Titan to the hotend so it's not as "direct" as one could imagine but still the print quality is excellent (or at least not impeded by the carriage). 

{{ super() }}

!!! tip "Custom Titan Tension Arm"

    ![Placeholder](assets/SSX.png){: align=left }

    The BOM contains my remix of the [E3D Titan Flex Upgrade](https://www.thingiverse.com/thing:2426505) thing which improves the Titan filament path greatly.

    My remix improves it's printability - print on the side where the spring is. No supports are needed.

    You can ommit the `SSX_tensioner_thing_2426505` part from the BOM if you plan on using the original arm.

!!! info "Universal EVA Front"

    This drive uses the universal face, which means it's compatible with all hotends you can find in the Hotends section.

{% endblock description %}
