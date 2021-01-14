#!/bin/bash

cp -f config.yaml complete/config.yaml
cp -f config.yaml contigs/config.yaml

#source /usr/local/anaconda3//etc/profile.d/conda.sh
#conda activate snakemake

##############################################################
# Run complete first! Necessary to download all dependecies. #
# Download pVOGs.hmm manually.				     #
##############################################################

cd complete/ 
snakemake -n --use-conda --cores all

cd ../contigs/
snakemake -n --use-conda --cores all
#conda deactivate
