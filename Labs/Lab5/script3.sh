#!/bin/bash

# Loop through all FASTA files in the current directory
for file in *.fasta; do
    if [ -f "$file" ]; then
        echo "File: $file"
        awk '/^>/ {print}' "$file"
    fi
done