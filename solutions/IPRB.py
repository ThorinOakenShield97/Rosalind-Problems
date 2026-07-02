k,m,n = map(int,input().split())

t = k + m + n

cross_1 = 1* (n/t) * ((n-1)/(t-1))
cross_2 = 0.25 * m/t * (m-1)/(t-1)
cross_3 = (m*n)/(t*(t-1))

recessive = cross_1 + cross_2 + cross_3

dominant = 1 - recessive
    
print(dominant)