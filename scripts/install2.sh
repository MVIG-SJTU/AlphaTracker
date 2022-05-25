#!/bin/bash
. ~/anaconda3/etc/profile.d/conda.sh

conda_path=$(which _conda)
sub_path="/etc/profile.d/conda.sh"
conda_real=". "${conda_path/_conda/$sub_path}
echo $conda_real
eval $conda_real

find_in_conda_env(){
    conda env list | grep "${@}" >/dev/null 2>/dev/null
}

conda config --append channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda clean -i

if find_in_conda_env ".*alphatracker.*" ; then
    conda activate alphatracker
else
    conda create -n alphatracker python=3.8 -y
    conda activate alphatracker
fi;


# Install pytorch
# conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch -c conda-forge -y

# Replace the above command with the following two commands if you locates in mainland, China.

conda config --add channels http://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c conda-forge -y
