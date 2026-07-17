import sys

def reverse(sequence):
    rev_comp = ''
    rev = sequence[::-1]
    for letter in rev:
        if letter == 'A':
            rev_comp += 'T'
        elif letter =='T':
            rev_comp +='A'
        elif letter =='C':
            rev_comp +='G'
        elif letter =='G':
            rev_comp +='C'
    
    return rev_comp

sequence = ''

for line in sys.stdin:
    if line.startswith('>'):
        ID = line[1:]
    else:
        sequence += line.strip()

for i in range(len(sequence)):
    for j in range(4,13):
        dna = sequence[i:i+j]
        if len(dna) == j:
            rev_dna = reverse(dna)
            if rev_dna == dna:
                print(i+1, len(dna))