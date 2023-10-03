#!bin/bash

filename=$1

while IFS= read -r line; do
	charCount=${#line}
	echo "Line: $line, Char count: $charCount"
done < "$filename"
	