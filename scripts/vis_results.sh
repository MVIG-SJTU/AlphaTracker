#!/bin/bash

# if result button is clicked, this script will be called

echo vis_results start


. ~/anaconda3/etc/profile.d/conda.sh

conda_path=$(which _conda)
sub_path="/etc/profile.d/conda.sh"
conda_real=". "${conda_path/_conda/$sub_path}
echo $conda_real
eval $conda_real

conda activate alphatracker

cd ./UI

python server.py


echo vis_results over

