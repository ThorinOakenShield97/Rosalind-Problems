import sys

sequences = []

for line in sys.stdin:
    line = line.strip()
    if line.startswith('>'):
        sequences.append('')
    else:
        sequences[-1] += line
        
n = len(sequences[0])

profile = {'A':[0] * n,
           'C': [0] * n,
           'G': [0] * n,
           'T': [0] * n
           }

for sequence in sequences:
    for j in range(n):
        if sequence[j] == 'A':
            profile['A'][j] += 1
        elif sequence[j] =='C':
            profile['C'][j] += 1
        elif sequence[j] == 'G':
            profile['G'][j] += 1
        elif sequence[j] == 'T':
            profile['T'][j] += 1

consensus = ''
bases = ['A','C','G','T']

for j in range(n):
    max_count = -1
    best = ''
    
    for b in bases:
        if profile[b][j] > max_count:
            max_count = profile[b][j]
            best = b
    
    consensus += best
    
print(consensus)
for key in profile:
    print(f"{key}:", *profile[key])