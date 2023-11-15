#!/usr/bin/env/python3


def aa_function(protein_sequence, amino_acid):
    """Find the percentage of the given amino acid's occurrence in the protein sequence."""
    total_amino_acids = len(protein_sequence)
    amino_acid_count = protein_sequence.count(amino_acid)
    
    if total_amino_acids != 0:
        percentage = (amino_acid_count / total_amino_acids) * 100
        return round(percentage)
    else:
        return 0

# Assertions to verify the function
assert aa_function("MSRSLLRFLLFLLLLPPLP", "M") == 5
assert aa_function("MSRSLLRFLLFLLLLPPLP", "R") == 11
assert aa_function("MSRSLLRFLLFLLLLPPLP", "L") == 47
assert aa_function("MSRSLLRFLLFLLLLPPLP", "Y") == 0