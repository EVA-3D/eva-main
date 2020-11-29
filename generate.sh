#!/bin/bash

set -e

cd docs/drives

cd bowden
eva-3d unpack-stls bom/v6.csv downloads/bowden.zip stls
eva-3d unpack-stls bom/mosquito.csv downloads/bowden.zip stls

cd ../bmg
eva-3d unpack-stls bom/v6.csv downloads/BMG.zip stls
eva-3d unpack-stls bom/mosquito.csv downloads/BMG.zip stls

cd ../titan
eva-3d unpack-stls bom/v6.csv downloads/titan.zip stls
eva-3d unpack-stls bom/mosquito.csv downloads/titan.zip stls

cd ../aero
eva-3d unpack-stls bom/aero.csv downloads/aero.zip stls

cd ../../addons/mgn15
eva-3d unpack-stls bom/titan.csv downloads/mgn15.zip stls
eva-3d unpack-stls bom/generic.csv downloads/mgn15.zip stls
eva-3d unpack-stls bom/bmg.csv downloads/mgn15.zip stls

cd ../../addons/x_endstop
eva-3d unpack-stls bom/angled_mgn12.csv downloads/endstops.zip stls
eva-3d unpack-stls bom/angled_mgn15.csv downloads/endstops.zip stls
