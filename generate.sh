#!/bin/bash

set -e

eva-3d unpack-stls docs/drives/bowden/bom/e3d.csv downloads/Bowden.zip docs/drives/bowden/stls
eva-3d unpack-stls docs/drives/bowden/bom/mosquito.csv downloads/Bowden.zip docs/drives/bowden/stls
