s = input()
t = input()

l_s = len(s)
l_t = len(t)

position = 1

for i in range(l_s-l_t+1):
    if s[i:l_t+i] == t:
        position = i +1
        print(position, end=' ')