#!/bin/bash

# if install button is clicked, this script will be called

echo install start

. ~/anaconda3/etc/profile.d/conda.sh

conda create -n alphatracker python=3.8 -y

conda activate alphatracker
# conda env update --file environment.yml

# Install pytorch
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch -c conda-forge -y

export PATH=/usr/local/cuda/bin/:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64/:$LD_LIBRARY_PATH

python setup.py build develop

# Please first modify Makefile according to cuda version
cd ./Tracking/AlphaTracker/train_yolo/darknet/
make
cd ../../../../

cd ./Tracking/AlphaTracker/
python3 download.py


echo install over

