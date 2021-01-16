#!/bin/bash

cp -f config.yaml complete/config.yaml
cp -f config.yaml contigs/config.yaml

#source /usr/local/anaconda3//etc/profile.d/conda.sh
#conda activate snakemake

##############################################################
# Run complete first! Necessary to download all dependecies. #
# Download pVOGs.hmm manually.				     #
##############################################################

read -p 'Number of cores: ' cores

cd complete/ 
# nice -n 5 snakemake --use-conda --cores ${cores}

cd ../contigs/
nice -n 5 snakemake --use-conda --cores ${cores}
#conda deactivate
