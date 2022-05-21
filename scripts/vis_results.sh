#!/bin/bash

# if result button is clicked, this script will be called

echo vis_results start


. ~/anaconda3/etc/profile.d/conda.sh

conda activate alphatracker

cd ./UI

python server.py


echo vis_results over

