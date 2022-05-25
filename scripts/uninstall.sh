#!/bin/bash

# if uninstall button is clicked, this script will be called

. ~/anaconda3/etc/profile.d/conda.sh

conda_path=$(which _conda)
sub_path="/etc/profile.d/conda.sh"
conda_real=". "${conda_path/_conda/$sub_path}
echo $conda_real
eval $conda_real

conda remove --name alphatracker --all -y


echo uninstall over


