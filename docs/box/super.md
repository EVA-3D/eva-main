---
title: BOX
type: superbox
hide:
    - toc
---

!!! info "Vendors"

    This whole page is just a convinience page for vendors if you are a normal EVA user this page **will not give you the expected results**.

# Super BOX

This is the SuperBOM generator. It's mostly like the normal BOX but instead of aggregating the parts with the `Sum` function it's using the `Max` function. 

In detail - if you add two components where one require `1x M3 nut` and the other `2x M3 nut` the normal BOM will tell you `3x M3  nut` while the SuperBOM will only caunt the biggest entry - resulting with `2x M3 nut`.

Ideally then one should create mutilple SuperBOMs and aggregate outside of this interface:

1. Drive SuperBOM
2. Hotend SuperBOM
3. Addons SuperBOM

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
    <h2>BOM</h2>
    <p>
        The table bellow contains an aggreegated bill of materials that sums up the bills of materials from the items that are in the box.
    </p>
    <p>
        You can select this table and copy/paste it to a spreadsheet.
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
    <img src="../../assets/404.png">
</div>


??? question "Local Storage"

    The box is stored in the *Local Storage* of you browser and will be purged  when it recognizes that the contents were gathered on an older version of EVA. This feature **does not store** any user identifying data.
