n = int(input())

def factorial(n:int)->int:
    product = 1
    if n == 0:
        return 1
    
    return n * factorial(n-1)

def gene_order(remaining:list, file, actual=[]):
    if len(remaining) == 0:
        file.write(' '.join(map(str,actual)) + '\n')
        return
    
    for chosen in remaining:
        order = [x for x in remaining if x != chosen]
        gene_order(order, file, actual +[chosen])
        

remaining = list(range(1,n+1))

with open('file.txt', 'w') as file:
    file.write(str(factorial(n)) + '\n')
    gene_order(remaining,file)
    


