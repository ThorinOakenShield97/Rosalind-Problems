DNA = input()

RNA = ''

for nucl in DNA:
    if nucl == 'T':
        RNA += 'U'
    else:
        RNA += nucl
           
print(RNA)