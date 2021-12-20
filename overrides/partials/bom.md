## Bill of materials

{% if meta.type == "drive" or meta.type == "hotend" %}

!!! info "PTFE Tube lengths"

    I have split the lengths into two, the drive side and the hotend side. **You need to sum the two lenghts from this and the {% if meta.type == "drive" %}hotend{% else %}drive{% endif %} BOM you'd be using.** (preferrably get more PTFE)
    
    **Do not cut the PTFE into two pieces**

{% endif %}

{{ get_bom() | md_table }}
