#!bin/bash

file=$1
line1=$2
line2=$3

sed -n "${line1},${line2}p" "$file"

#bash script3.sh file.tsv 2 5