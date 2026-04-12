#!/bin/bash

if [ $# -eq 0 ]
then
	echo "Usage: $0 <number of requests>"
	exit 1
fi

for ((i=0; i<$1; i++))
do 
	curl -I "https://komarev.com/ghpvc/?username=Benjamincf0&color=blue"
done
