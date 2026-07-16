import sys

dna_codons = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


def look_orfs():
    dna = ''

    for line in sys.stdin:
        if line.startswith('>'):
            ID = line[1:]
        else:
            dna += line.strip()
        

    reverse_dna = dna[::-1]
    compl = ''
    for letter in reverse_dna:
        if letter in bases:
            compl += bases[letter]
        
    triplets = ''
    orfs = set()
    
    for sequence in (dna,compl):
        for i in range(len(sequence)):
            if sequence[i:i+3] == 'ATG':
                for j in range(i,len(sequence),3):
                    triplets = sequence[j:j+3]
                    if triplets in ('TAA','TAG','TGA'):
                        orf_dna = sequence[i:j]
                        protein = ''
                        for k in range(0,len(orf_dna),3):
                            codon = orf_dna[k:k+3]
                            if codon in dna_codons:
                                protein += dna_codons[codon]
    
                        orfs.add(protein)
                        break

    return orfs

results = look_orfs()

for orf in results:
    print(orf)
