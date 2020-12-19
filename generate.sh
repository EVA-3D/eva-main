#!/bin/bash

set -e

cd docs/drives

cd bowden
eva-3d unpack-stls bom/v6.csv downloads/bowden.zip stls --remove_stl_dir
eva-3d unpack-stls bom/mosquito.csv downloads/bowden.zip stls

cd ../bmg
eva-3d unpack-stls bom/v6.csv downloads/bmg.zip stls --remove_stl_dir
eva-3d unpack-stls bom/mosquito.csv downloads/bmg.zip stls

cd ../titan
eva-3d unpack-stls bom/v6.csv downloads/titan.zip stls --remove_stl_dir
eva-3d unpack-stls bom/mosquito.csv downloads/titan.zip stls

cd ../aero
eva-3d unpack-stls bom/aero.csv downloads/aero.zip stls --remove_stl_dir

cd ../hemera
eva-3d unpack-stls bom/hemera.csv downloads/hemera.zip stls --remove_stl_dir

cd ../../addons/mgn15
eva-3d unpack-stls bom/titan.csv downloads/mgn15.zip stls --remove_stl_dir
eva-3d unpack-stls bom/generic.csv downloads/mgn15.zip stls
eva-3d unpack-stls bom/bmg.csv downloads/mgn15.zip stls
eva-3d unpack-stls bom/aero.csv downloads/mgn15.zip stls
eva-3d unpack-stls bom/hemera.csv downloads/mgn15.zip stls

