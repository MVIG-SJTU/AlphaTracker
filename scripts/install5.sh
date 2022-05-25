#!/bin/bash
. ~/anaconda3/etc/profile.d/conda.sh

conda_path=$(which _conda)
sub_path="/etc/profile.d/conda.sh"
conda_real=". "${conda_path/_conda/$sub_path}
echo $conda_real
eval $conda_real

conda activate alphatracker

cd ./Tracking/AlphaTracker/
python download.py
python download_check.py

echo finish