s = input()

s_reversed = reversed(s)

sc = ''

for elem in s_reversed:
    if elem == 'A':
        sc += 'T'
    elif elem == 'T':
        sc += 'A'
    elif elem == 'C':
        sc += 'G'
    elif elem == 'G':
        sc += 'C'
        
print(sc)