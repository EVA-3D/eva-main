#!/bin/bash

set -e

cd docs/drives

cd bowden
eva-3d unpack-stls bom/e3d.csv downloads/bowden.zip stls
eva-3d unpack-stls bom/mosquito.csv downloads/bowden.zip stls

cd ../bmg
eva-3d unpack-stls bom/e3d.csv downloads/BMG.zip stls
eva-3d unpack-stls bom/mosquito.csv downloads/BMG.zip stls

cd ../titan
eva-3d unpack-stls bom/e3d.csv downloads/titan.zip stls
eva-3d unpack-stls bom/mosquito.csv downloads/titan.zip stls
