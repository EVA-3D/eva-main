---
title: Introduction
---
# EVA <sub><sup>{{ config.version }}</sup></sub>

<iframe id="player" type="text/html" width="800" height="480"
  src="https://www.youtube.com/embed/fOFlQ7dKGFQ?enablejsapi=1&origin=https://eva-3d.github.io/eva-main/"
  frameborder="0"></iframe>

## Platform

EVA is a carriage platform for MGN rail based printers. The main goal is to support what people may have laying around or have easy access to. EVA is trying to implement that goal.

The specification is described in a separate {{ eva_link("spec") }} document.

### Parts explained

The _Bowden_ variant is the parent of all other drive variants in EVA 2.

The main parts (==sub assemblies==) of EVA 2 are:

- **front** - which changes based on the choosen hotend, e.g. E3D V6 vs a Mosquito.
- **top** - specified by the preferred drive - in this case there is no drive as for a bowden assembly a 3rd party drive is on the frame.
- **back** - different for motion systems - CoreXY is the default.
- **bottom** - mainly serves the purpose of being a proxy to a fan duct.

Then there are auxilary parts: **fan duct**, **belt grabbers**, **belt tensioners**, **probe holders**, **cable guides** and **shrouds**.

## Download

The whole package can be downloaded as a ZIP package, otherwise you can navigate to the the specific drive or addon page and download files from there.

[Download :octicons-download-24:]({{download_url}}){: .md-button .md-button--primary }

## Support

Big thanks to the users - one example is that only thanks to your donations the Mosquito parts were possible.

If you want to support the project or just buy me coffee you can [:fontawesome-brands-paypal: Paypal.me](https://www.paypal.me/pkucmus).

The project also received or receives continuous support from the companies we all know. Big thank you!

<p class="sponsors">
    <a href="https://www.ratrig.com/" >
        <img src="assets/ratrig.png" height="200"/>
    </a>
    <a href="https://www.bondtech.se/">
        <img src="assets/bondtech.png" height="200"/>
    </a>
</p>

Please go and buy something from them :smile:

### Issues

Issues, problems, feature requests, requests for compatibility with different printers can be requested in the project's [issue tracker](https://github.com/EVA-3D/eva-main/issues).

### Attributions

One does not need a keen eye to see that this design is based on many different designs that are out in the wild - although all the parts here are made from scratch - their authors deserve credit (their work provided inspiration):

* [Rat Rig](https://www.ratrig.com/) for making the V-core which is the perfect sanbox for building and modding a 3D Printer
* [pekcitron](https://www.thingiverse.com/pekcitron/about) for the [Prusa Bear Upgrade](https://www.thingiverse.com/thing:2808408)
* [BLV](https://www.thingiverse.com/BLV/about) and his amazing [BLV mgn cube](https://www.thingiverse.com/thing:3382718)

The following people deserve special credit for their amazing work - making some of the parts, providing guidance, testing parts, keeping me in check. Their input was a huge help so please do me a favor and check out their work:

* [Olof Ogland](http://www.olofogland.se)
* [Simon Davie](http://www.nexxdesign.co.uk)
* [João Barros](http://www.joaobarros.pt)

THANK YOU!

## Examples

For Rat Rig V-core Pro the [Easy Mod](https://github.com/pkucmus/Easy-Mod) is required to change the X and Y rail orientation.

EVA is now officially used by Rat Rig in their products :tada: :

* [V-core Pro (with Easy Mod)](https://www.ratrig.com/3d-printing-cnc/3d-printer-kits/complete-kits/rat-rig-v-core-pro-linear-rail-701.html)
* [V-cast](https://www.ratrig.com/3d-printing-cnc/3d-printer-kits/complete-kits/rat-rig-v-cast.html)

## Contact

If you need a more direct contact I'm on the [Rat Rig Unofficial Discord Server](https://discord.gg/DcCEk8u) along with many awesome people that will surely help :smile:

