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

def count_repeats(sequences):
    at_count = 0
    gc_count = 0
    for sequence in sequences.values():
        at_count += sequence.count("AT")
        gc_count += sequence.count("GC")
    return at_count, gc_count

def sequence_lengths(sequences):
    lengths = {header: len(sequence) for header, sequence in sequences.items()}
    return lengths

def count_ecor1_sites(sequences):
    ecor1_count = 0
    for sequence in sequences.values():
        ecor1_count += sequence.count("GAATTC")
    return ecor1_count

def replace_t_with_u(sequences):
    for header, sequence in sequences.items():
        sequences[header] = sequence.replace("T", "U")
    return sequences

def calculate_at_gc_content(sequences):
    at_content = {}
    gc_content = {}
    for header, sequence in sequences.items():
        length = len(sequence)
        at_count = sequence.count("A") + sequence.count("T")
        gc_count = sequence.count("G") + sequence.count("C")
        at_percentage = (at_count / length) * 100
        gc_percentage = (gc_count / length) * 100
        at_content[header] = at_percentage
        gc_content[header] = gc_percentage
    return at_content, gc_content

# Read sequences from the FASTA file
sequences = read_fasta_file("example2.fasta")

# Count AT and GC repeats
at_count, gc_count = count_repeats(sequences)
print(f"Total AT repeats: {at_count}")
print(f"Total GC repeats: {gc_count}")

# Find the length of each sequence
lengths = sequence_lengths(sequences)
for header, length in lengths.items():
    print(f"Sequence {header} has a length of {length} nucleotides.")

# Count the number of EcoR1 sites
ecor1_count = count_ecor1_sites(sequences)
print(f"Total EcoR1 sites (G*AATTC): {ecor1_count}")

# Replace T with U and save in a new file
sequences_with_u = replace_t_with_u(sequences)
with open("RNAconverted.fna", "w") as output_file:
    for header, sequence in sequences_with_u.items():
        output_file.write(f">{header}\n{sequence}\n")

# Calculate AT and GC content as percentages
at_content, gc_content = calculate_at_gc_content(sequences)
for header in at_content.keys():
    print(f"AT content of {header}: {at_content[header]:.2f}%")
    print(f"GC content of {header}: {gc_content[header]:.2f}%")


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
