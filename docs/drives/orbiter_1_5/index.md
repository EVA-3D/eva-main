---
title: Orbiter 1.5
icon: material/cog-pause
uid: EVA / Orbiter 1.5
type: drive
spec: 2.4.0
badges:
    - official
contributors: 
    - pkucmus
cad_url: https://cad.onshape.com/documents/bb8303124bc8370b6d1924bc/w/8276a22c579374e8b02e9b96/e/6b8206d26df549409bc1d1b2
satisfies:
    - drive
usage: 0.522
---

{% extends 'drives.md' %}

{% block description %}

EVA 2 supports [The Orbiter](https://www.thingiverse.com/thing:4725897){target=_blank} created by dr Robert Lorincz. 
You can also check other [Orbiter Projects here](https://orbiterprojects.com/){target=_blank}.

Since EVA 2.2.1 Orbiter 1.0 was deprecated and removed.
Orbiter 1.5 is also going away in favor of [Orbiter 2.0](/drives/orbiter_2_0/).

??? info "Orbiter 1.0 users"

    Old parts supporting the old Orbiter can be found in git history on tag [2.2.0](https://github.com/EVA-3D/eva-orbiter/tree/2.2.0/stls){target=_blank}

{{ super() }}

(Survey result is shared with [Orbiter 2.0](/drives/orbiter_2_0/))

!!! info "Universal EVA Front"

    This drive uses the universal face, which means it's compatible with all hotends you can find in the Hotends section.

{% endblock description %}
