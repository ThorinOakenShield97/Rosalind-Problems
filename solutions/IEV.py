import sys

line = sys.stdin.readline().strip()
nums = line.split()

genotypes = [int(x) for x in nums]
probs = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]

total = 0
for i,j in zip(genotypes,probs):
    total += 2*i*j

print(total)