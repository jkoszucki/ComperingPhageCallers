#!/bin/bash

source /usr/local/anaconda3//etc/profile.d/conda.sh
conda activate snakemake

##############################################################
# Run complete first! Necessary to download all dependecies. #
# Download pVOGs.hmm manually.				     #
##############################################################

cd complete/ 
snakemake --use-conda --cores all

cd ../contigs/
snakemake --use-conda --cores all
conda deactivate
