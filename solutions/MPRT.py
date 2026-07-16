import urllib.request
import re
import ssl

pattern = "(?=(N[^P][ST][^P]))"

with open('rosalind_mprt.txt', 'r') as archive:
    content = archive.read()
    
ids = content.split('\n')
context = ssl._create_unverified_context()

for ID in ids:
    uniprot_ID = ID.split('_')[0]
    url = f"http://www.uniprot.org/uniprot/{uniprot_ID}.fasta"
    answer = urllib.request.urlopen(url, context=context)
    text = answer.read().decode('utf-8')
    lines = text.split('\n')
    sequence = ''.join(lines[1:])

    positions = []

    for elem in re.finditer(pattern, sequence):
        position = elem.start(1) +1
        positions.append(str(position))


    if positions:
        print(ID)
        print(' '.join(positions))
