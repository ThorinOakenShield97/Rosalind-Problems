import sys

results = {}

for line in sys.stdin:
    line = line.strip()
    
    if line.startswith('>'):
        ID = line[1:]
        results[ID] = results.get(ID,'')
    else:
        results[ID] += line

max_GC = 0
max_ID = ''

for ID in results:
    total = len(results[ID])
    GC = 0
    for letter in results[ID]:
        if letter == 'G' or letter == 'C':
            GC += 1
    GC_perc = GC/total * 100
    if GC_perc > max_GC:
        max_GC = GC_perc
        max_ID = ID

print(max_ID)
print(max_GC)
        
        
    
        
    