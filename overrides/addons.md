# {{ meta.title }}

{% block header %}
{% endblock header %}

![preview](assets/{{meta.uid|safe_filename}}.png)

## Description

{% block description %}
- authors: {% for contributor in meta.contributors %}[{{contributor}}](https://github.com/{{contributor}}){% endfor %}
{% for badge in meta.badges %}- {{badge}}
{% endfor %}
{% endblock description %}

{% include 'partials/bom.md' %}

## Links

{{ download_button }}

{% include 'partials/looking_for_files.md' %}
