#!/usr/bin/env/python3

def read_fasta_file(filename):
    sequences = {}
    current_sequence = ""
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if current_sequence:
                    sequences[header] = current_sequence
                header = line[1:]  # Remove the ">" character
                current_sequence = ""
            else:
                current_sequence += line
        if current_sequence:
            sequences[header] = current_sequence
    return sequences

# Read sequences from the FASTA file
sequences = read_fasta_file("pUC19c.fasta")

# a. Join the sequence together and exclude the header
sequence = "".join(list(sequences.values())[0])

# b. Count the number of SmaI sites (CCCGGG)
smai_count = sequence.count("CCCGGG")

# c. Calculate AT and GC content as percentages
total_length = len(sequence)
at_count = sequence.count("A") + sequence.count("T")
gc_count = sequence.count("G") + sequence.count("C")
at_percentage = (at_count / total_length) * 100
gc_percentage = (gc_count / total_length) * 100

# Print the results
print("Joined sequence (excluding header):")
print(sequence)

print(f"Total SmaI sites (CCCGGG): {smai_count}")

print(f"AT content: {at_percentage:.2f}%")
print(f"GC content: {gc_percentage:.2f}%")
