#!/usr/bin/env/python3

# Define the filename
filename = "example2.fasta"

# Initialize a counter for the number of sequences
sequence_count = 0

# Open the file for reading
with open(filename, "r") as file:
    in_sequence = False  # Flag to track whether we are inside a sequence block

    # Iterate through each line in the file
    for line in file:
        if line.startswith(">"):
            sequence_count += 1

# Print the total number of sequences
print(f"Total number of sequences in {filename}: {sequence_count}")
