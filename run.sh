#!/bin/bash

##############################################################
# Run complete first! Necessary to download all dependecies. #
# Download pVOGs.hmm manually. Install locally wgsim!	     #
##############################################################

read -p "ios or linux?  >>  " os
read -p "Number of cores  >>  " cores

export cores
export os
bash scripts/prepare-envs.sh

cd complete/ 
nice -n 5 snakemake --use-conda --cores ${cores} -R

cd ../contigs/
nice -n 5 snakemake --use-conda --cores ${cores} -R
