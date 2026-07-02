n = int(input())
m = int(input())

ages = [0]*m
ages[0] = 1
new_ages = [0] * m


for i in range(n-1):
    newborns = sum(ages[1:])
    new_ages = [0] * m
    new_ages[0] = newborns
    
    for j in range(1,m):
        new_ages[j] = ages[j-1]
    
    ages = new_ages[:]

print(sum(ages))