#!/bin/bash

set -e

cd docs/drives

cd bowden
eva-3d unpack-stls bom/BOM_[Assembly]_V6.csv downloads/Bowden.__ALL__.zip stls --remove_stl_dir
eva-3d unpack-stls bom/BOM_[Assembly]_mosquito.csv downloads/Bowden.__ALL__.zip stls
eva-3d unpack-stls bom/BOM_[Assembly]_dragon.csv downloads/Bowden.__ALL__.zip stls
eva-3d unpack-stls bom/BOM_Bowden.MGN15.csv downloads/Bowden.MGN15.zip stls

cd ../bmg
eva-3d unpack-stls bom/BOM_[Assembly]_V6.csv downloads/BMG.__ALL__.zip stls --remove_stl_dir
eva-3d unpack-stls bom/BOM_[Assembly]_mosquito.csv downloads/BMG.__ALL__.zip stls
eva-3d unpack-stls bom/BOM_[Assembly]_dragon.csv downloads/BMG.__ALL__.zip stls
eva-3d unpack-stls bom/BOM_BMG.MGN15.csv downloads/BMG.MGN15.zip stls

cd ../titan
eva-3d unpack-stls bom/BOM_[Assembly]_V6.csv downloads/Titan.__ALL__.zip stls --remove_stl_dir
eva-3d unpack-stls bom/BOM_[Assembly]_mosquito.csv downloads/Titan.__ALL__.zip stls
eva-3d unpack-stls bom/BOM_[Assembly]_dragon.csv downloads/Titan.__ALL__.zip stls
eva-3d unpack-stls bom/BOM_Titan.MGN15.csv downloads/Titan.MGN15.zip stls

cd ../orbiter
eva-3d unpack-stls bom/BOM_[Assembly]_V6.csv downloads/Orbiter.__ALL__.zip stls --remove_stl_dir
eva-3d unpack-stls bom/BOM_[Assembly]_mosquito.csv downloads/Orbiter.__ALL__.zip stls
eva-3d unpack-stls bom/BOM_[Assembly]_dragon.csv downloads/Orbiter.__ALL__.zip stls
eva-3d unpack-stls bom/BOM_Orbiter.MGN15.csv downloads/Orbiter.MGN15.zip stls
eva-3d unpack-stls bom/cr_10.csv downloads/Orbiter.__ALL__.zip stls
eva-3d unpack-stls bom/cr_10.csv downloads/Orbiter.MGN15.zip stls

cd ../aero
eva-3d unpack-stls bom/BOM_Aero.__ALL__.csv downloads/Aero.__ALL__.zip stls --remove_stl_dir
eva-3d unpack-stls bom/BOM_Aero.MGN15.csv downloads/Aero.MGN15.zip stls

cd ../hemera
eva-3d unpack-stls bom/BOM_Hemera.__ALL__.csv downloads/Hemera.__ALL__.zip stls --remove_stl_dir
eva-3d unpack-stls bom/BOM_Hemera.MGN15.csv downloads/Hemera.MGN15.zip stls

cd ../../addons/cartesian_idex
eva-3d unpack-stls bom/cartesian.csv downloads/cartesian_idex.zip stls --remove_stl_dir
eva-3d unpack-stls bom/idex_x1.csv downloads/cartesian_idex.zip stls
eva-3d unpack-stls bom/idex_x2.csv downloads/cartesian_idex.zip stls

cd ../../..

echo "Copying all *.stl to stls"
rm stls/*
find . -name \*.stl -exec cp {} stls \;

echo "Packing stls"
rm stls.zip || true
zip -9 -r stls.zip stls

