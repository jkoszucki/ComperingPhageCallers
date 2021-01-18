#!/bin/bash

read -p "ios or linux?  >>  " os
echo $(pwd)
cd envs/

if [[ ${os} = 'ios' ]]
then
	cd ios-envs
	for f in *; do cp -f ${f} ../${f%?????????}.yaml; done

elif [[ ${os} = 'linux' ]]
then
	cd linux-envs
	for f in *; do cp -f ${f} ../${f%???????????}.yaml; done
else
	echo 'Wrong name'
fi


