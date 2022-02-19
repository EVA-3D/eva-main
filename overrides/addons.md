# {{ meta.title }}

{% block header %}
{% endblock header %}

![preview](assets/{{eva.uid|slugify}}.png)

## Description

{% block description %}
- authors: {% for contributor in eva.contributors %}[{{contributor}}](https://github.com/{{contributor}}){% endfor %}
{% for badge in eva.badges %}- {{badge}}
{% endfor %}
{% endblock description %}

{% include 'partials/bom.md' %}

## Links

{{ download_button }}

{% include 'partials/looking_for_files.md' %}
