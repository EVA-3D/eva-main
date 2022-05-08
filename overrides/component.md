{% block header %}
??? info inline end "Inserts and Nuts"
    {% if meta.eva.mounting == "heat_insert" %}
    ![](/assets/inserts_small.png){ align=right }
    This is a **heat insert** variant of this component, looking for the [hex nut](/hex_nuts/{{meta.eva.category}}/{{meta.eva.component}}) variant?
    {% elif meta.eva.mounting == "hex_nuts" %}
    ![](/assets/hex_nuts_small.png){ align=right }
    This is a **hex nut** variant of this component, looking for the [heat insert](/heat_insert/{{meta.eva.category}}/{{meta.eva.component}}) variant?
    {% endif %}
{% endblock header %}

# {{ meta.title }}

{% if assembly_data(meta.eva.name).get("description") %}
## Description

{% block description %}
{{ assembly_data(meta.eva.name).get("description") }}
{% endblock description %}
{% endif %}

![preview](/onshape_assets/{{meta.eva.name|lower}}.png)

## Bill of Materials

For {{ meta.eva.component }}

{{ get_bom(meta.eva.name) | md_table() }}

## Links

!!! info "STEP files? CAD Link?"

    If you are looking for the CAD link to tamper with the design or to export the parts in formats other than STL you can find the links below.  
    **Be warned though!** The link directs to a live - bleeding edge - version of this particular EVA module - there is no promise it will be the same version as what you see above nor does it have to be the version Rat Rig provides.

    ??? warning "I understand, please give me the link"

        {{ get_cad_link(meta.eva.name) }}


