#!bin/bash

tsv=$1


sed 's/\t/,/g' $1 > file.csv

echo $file.csv

#bash script.sh file.tsv