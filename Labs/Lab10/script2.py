#!/usr/bin/env/python3

import argparse
from Bio import SeqIO

def load_fasta_file(file_path):
    """Load a given fasta file."""
    sequences = list(SeqIO.parse(file_path, "fasta"))
    return sequences
    
def find_sequence_lengths_and_percentage(sequences):
    """Find the length of each sequence and the percentage of specified amino acids."""
    amino_acids_to_count = ['M', 'L', 'R', 'Y']

    for sequence in sequences:
        length = len(sequence.seq)
        print(f"Sequence Length: {length}")

        amino_acid_counts = {acid: sequence.seq.count(acid) for acid in amino_acids_to_count}
        total_amino_acids = sum(amino_acid_counts.values())

        if total_amino_acids != 0:
            for acid in amino_acids_to_count:
                percentage = (amino_acid_counts[acid] / total_amino_acids) * 100
                print(f"Percentage of {acid}: {percentage:.2f}%")
        else:
            print("No amino acids found in the sequence.")

        print("\n")

def test_methionine_start(sequences):
    """Test if each sequence starts with Methionine (M)."""
    for i, sequence in enumerate(sequences, start=1):
        starts_with_methionine = sequence.seq.startswith('M')
        status = "starts" if starts_with_methionine else "does not start"
        print(f"Sequence {i} {status} with Methionine")

def count_sequences(sequences):
    """Count the number of sequences, sequences starting with Methionine, and sequences not starting with Methionine."""
    total_sequences = len(sequences)
    methionine_start = sum(sequence.seq.startswith('M') for sequence in sequences)
    non_methionine_start = total_sequences - methionine_start

    print(f"Total Sequences: {total_sequences}")
    print(f"Sequences starting with Methionine: {methionine_start}")
    print(f"Sequences not starting with Methionine: {non_methionine_start}")

def validate_methionine_count(sequences):
    """Validate the number of sequences that start with Methionine."""
    methionine_start = sum(sequence.seq.startswith('M') for sequence in sequences)
    assert methionine_start == 68, "Validation failed: The number of sequences starting with Methionine is not 68."

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a fasta file.")
    parser.add_argument("fasta_file", help="Path to the fasta file")

    args = parser.parse_args()
    fasta_file_path = args.fasta_file

    # Load fasta file
    fasta_sequences = load_fasta_file(fasta_file_path)

    # a. Find the length of each sequence and the percentage of specified amino acids.
    find_sequence_lengths_and_percentage(fasta_sequences)

    # b. Test if each sequence starts with Methionine.
    test_methionine_start(fasta_sequences)

    # c. Count the number of sequences, sequences starting with Methionine, and sequences not starting with Methionine.
    count_sequences(fasta_sequences)

    # d. Validate the number of sequences that start with Methionine.
    validate_methionine_count(fasta_sequences)
