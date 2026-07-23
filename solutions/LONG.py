import sys

def fusion(fragments,half):
    results = {}
    for frag in fragments:
        if frag[:half] not in results:
            results[frag[:half]] = []
        results[frag[:half]].append(frag)
        
    for i in range(len(fragments)):
        frag1 = fragments[i]
        for k in range(len(frag1), half, -1):
            sufix = frag1[-k:]
            key = sufix[:half]
            if key in results:
                for frag2 in results[key]:
                    if sufix == frag2[:k] and frag1 != frag2:
                        seq = frag1 + frag2[k:]
                        fragments.append(seq)
                        fragments.remove(frag1)
                        fragments.remove(frag2)   
                        return True                      
    return False

sequence = ''
fragments = []

for line in sys.stdin:
    if line.startswith('>'):
        if len(sequence) != 0:
            fragments.append(sequence)
            sequence = ''
        ID = line[1:]
    else:
        sequence += line.strip()
    
fragments.append(sequence)
half = min(len(f) for f in fragments) // 2
        
while len(fragments) > 1 and fusion(fragments,half):
    pass

print(fragments[0])
