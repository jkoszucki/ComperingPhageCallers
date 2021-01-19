#!/bin/bash

##############################################################
# Run complete first! Necessary to download all dependecies. #
# Download pVOGs.hmm manually. Install locally wgsim!	     #
##############################################################

read -p "ios or linux?  >>  " os
read -p "Number of cores  >>  " cores

cwd=$(pwd)

#./scripts/dependecies.sh
cp -f config.yaml complete/config.yaml
cp -f config.yaml contigs/config.yaml

if [[ ${os} = 'ios' ]]
then
	cd envs/ios-envs
	for f in *; do cp -f ${f} ../${f%?????????}.yaml; done

elif [[ ${os} = 'linux' ]]
then
	cd envs/linux-envs
	for f in *; do cp -f ${f} ../${f%???????????}.yaml; done
else
	echo 'Wrong name'
fi

cd ${cwd} 
cd complete/ 
snakemake --use-conda --cores ${cores} -R --conda-create-envs-only

cd ../contigs/
snakemake --use-conda --cores ${cores} -R --conda-create-envs-only

