#!/bin/bash

amino_acids=("Methionine" "Leucine" "Cysteine" "Alanine" "Valine" "Tyrosine" "Proline")

for amino_acid in "${amino_acids[@]}"; do
    # Calculate the length of the amino acid string
    length=${#amino_acid}
    # Print the amino acid and its length
    echo "Amino Acid: $amino_acid, Length: $length"
done