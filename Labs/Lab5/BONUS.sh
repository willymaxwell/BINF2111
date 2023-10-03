#!/bin/bash

# Define the input file
input_file="example2.fasta"

# Define the output file for the converted sequences
output_file="converted.fasta"

# Initialize counters
atg_count=0
serine_count=0
arginine_count=0
stop_count=0

# Loop through the input file to count and convert sequences
while IFS= read -r line
do
    # Check if the line is a sequence line (starts with '>')
    if [[ $line == ">"* ]]; then
        echo "$line" >> "$output_file"
    else
        # Count ATG, S, R, and stops (*)
        atg_count=$((atg_count + $(grep -o "ATG" <<< "$line" | wc -l)))
        serine_count=$((serine_count + $(grep -o "S" <<< "$line" | wc -l)))
        arginine_count=$((arginine_count + $(grep -o "R" <<< "$line" | wc -l)))
        stop_count=$((stop_count + $(grep -o "TAA\|TAG\|TGA" <<< "$line" | wc -l)))

        # Replace sequences with single-letter codes
        line=$(sed -e 's/ATG/M/g' -e 's/S/S/g' -e 's/R/R/g' -e 's/TAA\|TAG\|TGA/*/g' <<< "$>        echo "$line" >> "$output_file"
    fi
done < "$input_file"

# Print the counts
echo "ATG (M): $atg_count"
echo "Serine (S): $serine_count"
echo "Arginine (R): $arginine_count"
echo "Stops (*): $stop_count"
