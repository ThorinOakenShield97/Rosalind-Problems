def binary_search(pi,tails,x):
    left = 0
    right = len(tails) -1
    
    while left < right:
        mid = (left + right) //2
        if pi[tails[mid]] < x:
            left = mid +1
        elif pi[tails[mid]] >= x:
            right = mid
        
    return left

def find_lis(pi):
    tails = []
    parents = [-1] * len(pi)
    for i,elem in enumerate(pi):
        if len(tails) ==0 or elem > pi[tails[-1]]:
            if len(tails) != 0:
                parents[i] = tails[-1]
            tails.append(i)
        else:
            index = binary_search(pi,tails,elem)
            if index > 0:
                parents[i] = tails[index-1]
            tails[index] = i
    
    results = []
    curr = tails[-1]

    while curr != -1:
        results.append(pi[curr])
        curr = parents[curr]
    
    results.reverse()
    return results


n = int(input())
pi = [int(x) for x in input().split()]
lis = find_lis(pi)

pi_negative = [-x for x in pi]
lds_negative = find_lis(pi_negative)
lds = [-x for x in lds_negative]


print(*lis)
print(*lds)