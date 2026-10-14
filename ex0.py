import collections
import matplotlib.pyplot as plt

def analyze_top_10_codons(file_path):
    print(f"Reading {file_path}...")
    
    sequence_lines = []
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('>'):
                sequence_lines.append(line.strip())
                
    full_sequence = "".join(sequence_lines).upper().replace('U', 'T')
    
    genetic_code = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'Stop', 'TAG':'Stop', 'TGC':'C', 'TGT':'C', 'TGA':'Stop', 'TGG':'W',
    }
    
    codons = []
    for frame in range(3):
        for i in range(frame, len(full_sequence) - 2, 3):
            codons.append(full_sequence[i:i+3])
            
    frequency_counts = collections.Counter(codons)
    top_10 = frequency_counts.most_common(10)
    
    labels = [item[0] for item in top_10]
    counts = [item[1] for item in top_10]
    amino_acids = [genetic_code.get(codon, '?') for codon in labels]
    
    #  Plot the Top 10
    plt.figure(figsize=(10, 6))
    plt.bar(labels, counts, color='mediumpurple', edgecolor='black')
    plt.title('Top 10 Most Frequent Codons in Genome', fontsize=14)
    plt.xlabel('Codon', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    
    # Label each bar with the count and its Amino Acid letter
    for i, count in enumerate(counts):
        plt.text(i, count + (max(counts) * 0.01), f"{count:,}\n({amino_acids[i]})", ha='center')
        
    plt.tight_layout()
    plt.show()
    
    return top_10

if __name__ == "__main__":
    results = analyze_top_10_codons("sequence.fasta")
    print("\n--- Top 10 Codons ---")
    for codon, count in results:
        print(f"{codon}: {count:,}")