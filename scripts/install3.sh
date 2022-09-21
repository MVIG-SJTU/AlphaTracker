#!/bin/bash
. ~/anaconda3/etc/profile.d/conda.sh

conda activate alphatracker

export PATH=/usr/local/cuda/bin/:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64/:$LD_LIBRARY_PATH
pip uninstall alphatracker -y
pip uninstall alphatracker -y
pip install Cython
python setup.py build develop
