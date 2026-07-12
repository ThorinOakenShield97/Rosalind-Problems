import sys

sequences = []
actual = []

for line in sys.stdin:
    line = line.strip()
    if line.startswith('>'):
        if actual:
            sequences.append(''.join(actual))
            actual = []
    
    else:
        actual.append(line)

if actual:
    sequences.append(''.join(actual))
    

shortest = min(sequences, key=len)
low = 1
high = len(shortest)
best = ''

while low <= high:
    found = ''
    mid = (low+high)//2
    motifs = set()
    for i in range(len(shortest)-mid+1):
        fragment = shortest[i:i+mid]
        motifs.add(fragment)
        
    for seq in sequences:
        motifs = {c for c in motifs if c in seq}
        
    if motifs:
        found = motifs.pop()
    
    if found:
        best = found
        low = mid + 1
    else:
        high = mid -1
        
print(best)
        