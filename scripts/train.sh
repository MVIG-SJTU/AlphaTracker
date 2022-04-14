#!/bin/bash

# if train button is clicked, this script will be called

echo train start


. ~/anaconda3/etc/profile.d/conda.sh

conda activate alphatracker

cd ./Tracking/AlphaTracker/

python train.py


echo train over


