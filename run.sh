#!/bin/bash

##############################################################
# Run complete first! Necessary to download all dependecies. #
# Download pVOGs.hmm manually. Install locally wgsim!	     #
##############################################################

./scripts/prepare-envs.sh

read -p 'Number of cores: ' cores

cd complete/ 
nice -n 5 snakemake --use-conda --cores ${cores} -R

cd ../contigs/
nice -n 5 snakemake --use-conda --cores ${cores} -R
