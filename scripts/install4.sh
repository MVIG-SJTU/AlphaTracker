#!/bin/bash
. ~/anaconda3/etc/profile.d/conda.sh

conda activate alphatracker

export PATH=/usr/local/cuda/bin/:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64/:$LD_LIBRARY_PATH

cd ./Tracking/AlphaTracker/train_yolo/darknet/
make clean
make -s
cd ../../../../
