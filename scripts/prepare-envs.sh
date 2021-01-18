#!/bin/bash

cp -f config.yaml complete/config.yaml
cp -f config.yaml contigs/config.yaml

##############################################################
# Run complete first! Necessary to download all dependecies. #
# Download pVOGs.hmm manually. Install locally wgsim!	     #
##############################################################

# Prepering environments on linux or ios.
./scripts/prepare-envs.sh
#./scripts/dependecies.sh

read -p 'Number of cores: ' cores

cd complete/ 
nice -n 5 snakemake --use-conda --cores ${cores} --conda-create-envs-only

cd ../contigs/
nice -n 5 snakemake --use-conda --cores ${cores} -R --conda-create-envs-only

