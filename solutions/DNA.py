DNA = input()

A,C,G,T = 0,0,0,0

for nucl in DNA:
    if nucl == 'A':
        A +=1
    elif nucl == 'C':
        C +=1
    elif nucl == 'G':
        G +=1
    elif nucl =='T':
        T += 1
    
print(f"{A} {C} {G} {T}")
