#!/bin/bash
. ~/anaconda3/etc/profile.d/conda.sh

conda activate alphatracker

cd ./Tracking/AlphaTracker/
python3 download.py