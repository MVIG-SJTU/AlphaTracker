#!/bin/bash

# if train button is clicked, this script will be called

echo train start


. ~/anaconda3/etc/profile.d/conda.sh

conda_path=$(which _conda)
sub_path="/etc/profile.d/conda.sh"
conda_real=". "${conda_path/_conda/$sub_path}
echo $conda_real
eval $conda_real

conda activate alphatracker

cd ./Tracking/AlphaTracker/

python train.py ui


echo train over


