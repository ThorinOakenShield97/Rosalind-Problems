import sys

codons = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2, 'I': 3, 'K': 2, 'L': 6,
    'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6, 'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2
}

total = 1
for line in sys.stdin:
    line = line.strip()
    
    for letter in line:
        total = (total*codons.get(letter,1)) % 1000000
    
total = total*3
total = total%1000000


print(total)
    