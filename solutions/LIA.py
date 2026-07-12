import math

nums = input().split()
k = int(nums[0])
objective = int(nums[1])

total = 2**k

acum = 0
for i in range(objective,total+1):
    prob = math.comb(total,i) * (0.25**i)*(0.75**(total-i))
    acum += prob

print(acum)
    