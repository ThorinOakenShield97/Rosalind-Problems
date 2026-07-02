def rabbits(n,k):
    
    def rabbits(n,k,memo):
        if n == 1 or n == 2:
            return 1
        
        if n in memo:
            return memo[n]
        
        else:
            memo[n] = rabbits(n-1,k,memo) + (k*rabbits(n-2,k,memo))
        return memo[n]
            
    memo = dict()
    
    return rabbits(n,k,memo)