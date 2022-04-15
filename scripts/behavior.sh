#!/bin/bash

# if behavior button is clicked, this script will be called

echo behavior start


. ~/anaconda3/etc/profile.d/conda.sh

conda activate alphatracker

cd ./BehavioralClustering

bash run_all.sh

python fft_main_sep_twoMiceInteract.py

echo behavior over

