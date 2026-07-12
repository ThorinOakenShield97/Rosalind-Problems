import sys

results = {}

for line in sys.stdin:
    line = line.strip()
    
    if line.startswith('>'):
        ID = line[1:]
        results[ID] = results.get(ID,'')
    else:
        results[ID] += line
        
for id1, seq1 in results.items():
    for id2, seq2 in results.items():
        if id1 != id2:
            if seq1[-3:] == seq2[:3]:
                print(id1,id2)