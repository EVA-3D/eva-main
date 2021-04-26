---
title: BOX
type: box
hide:
    - toc
---

??? warning "The Box feature is still being tested"

    Please feel free to use it, it was tested before release but never on a big scale. If there's anything wrong with the feature please file an issue on [GitHub](https://github.com/EVA-3D/eva-main/issues) or let `@McAbra` know on Discord.

# BOX <small>Your configuration</small>

This is **the box** - a feature of this documentation that is meant
to help you to figure out which parts you need to build your EVA carriage

Typically you will need a **drive**, **hotend**, **endstop** and a **bed probe**:

<div v-show="itemsCount">
    <table>
        <thead>
            <tr>
                <th role="columnheader">Type</th>
                <th role="columnheader">Name</th>
                <th role="columnheader">Satisfies</th>
                <th role="columnheader">Remove</th>
                <th role="columnheader">CAD</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(item, name, index) in items">{% raw %}
                <td>{{item.type}}</td>
                <td>{{name}}</td>
                <td>{{item.satisfies | join}}</td>{% endraw %}
                <td align="center">
                    <a v-on:click="remove(name)" class="remove">
                        {{ icon("fontawesome-solid-minus-circle") }}
                    </a>
                </td>
                <td align="center">
                    <a v-bind:href="item.cad_url" target="_blank">
                        {{ icon("fontawesome-solid-file-import") }}
                    </a>
                </td>
            </tr>
        </tbody>
    </table>
    <details v-bind:class="{warning: missing, success: !missing}">
        <summary>{% raw %}{{missing ? 'Missing items?' : 'All set!'}}{% endraw %}</summary>
        <div v-if="missing">
            <p>You might be missing items for a full EVA carriage:</p>
        </div>
        <p v-if="!missing">Great! You should shave all that you need to build an EVA!</p>
        <ul class="task-list">
            <li class="task-list-item" v-for="(satisfied, name) in satisfaction">
                <label class="task-list-control">
                    <input type="checkbox" disabled v-bind:value="name" v-model="satisfactionList">
                    <span class="task-list-indicator"></span>
                </label> {% raw %}{{ satisfiesMap[name] }}{% endraw %}
            </li>
        </ul>
    </details>
    <h2>BOM</h2>
    <p>
        The table bellow contains an aggreegated bill of materials that sums up the bills of materials from the items that are in the box.
    </p>
    <table>
        <thead>
            <tr>
                <th role="columnheader">Part</th>
                <th role="columnheader">Quantity</th>
                <th role="columnheader">Name</th>
                <th role="columnheader">Type</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(part, name, index) in parts">{% raw %}
                <td>{{index + 1}}</td>
                <td>{{part.qty}}</td>
                <td v-if="part.url"><a :href="part.url">{{part.name}}</a></td>
                <td v-if="!part.url">{{part.name}}</td>
                <td>{{part.type}}</td>
            {% endraw %}</tr>
        </tbody>
    </table>
</div>
<div v-show="!itemsCount">
    <p>
        Your box is empty, use the navigation on the left to find the
        components you are interested in and add them to your box.
    </p>
    <img src="../assets/404.png">
</div>


??? question "Local Storage"

    The box is stored in the *Local Storage* of you browser and will be purged  when it recognizes that the contents were gathered on an older version of EVA. This feature **does not store** any user identifying data.
