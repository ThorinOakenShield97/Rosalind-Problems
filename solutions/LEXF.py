letters = input().split()
n = int(input())

combinations = ['']

for i in range(n):
    combinations =[elem + letter for elem in combinations for letter in letters]
    

for comb in combinations:
    print(comb)