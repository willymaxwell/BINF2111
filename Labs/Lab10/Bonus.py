#!/usr/bin/env/python3

def calculate_gc_content(sequence):
    """Calculate the GC content of a DNA sequence."""
    gc_count = sequence.count('G') + sequence.count('C')
    total_bases = len(sequence)
    gc_content = (gc_count / total_bases) * 100
    return gc_content

def analyze_sequence(sequence):
    """Analyze the GC content of a DNA sequence."""
    gc_content = calculate_gc_content(sequence)

    if gc_content < 45:
        print("Low GC content (< 45%):")
    elif 45 <= gc_content < 65:
        print("Medium GC content (45-65%):")
    else:
        print("High GC content (65% or more):")

    print(f"GC content: {gc_content:.2f}%")
    print("Sequence:")
    print(sequence)
    print("\n")

if __name__ == "__main__":
    fasta_file_path = "example2.fasta"
    sequences = list(SeqIO.parse(fasta_file_path, "fasta"))

    for i, sequence in enumerate(sequences, start=1):
        print(f"Analyzing Sequence {i}:")
        analyze_sequence(str(sequence.seq))