s = input()
t = input()

dH = 0

for i in range(len(s)):
    if s[i] != t[i]:
        dH +=1
        
print(dH)