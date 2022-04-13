#!/bin/bash

# if track button is clicked, this script will be called

echo track start


. ~/anaconda3/etc/profile.d/conda.sh

conda activate alphatracker

cd ./Tracking/AlphaTracker/

python track.py


echo track over


