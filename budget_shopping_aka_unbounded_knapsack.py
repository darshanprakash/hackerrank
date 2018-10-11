def unboundedKnapsack(W, val, wt): 
    n = len(val)
    # dp[i] is going to store maximum  
    # value with knapsack capacity i. 
    dp = [0 for i in range(W + 1)] 
  
    ans = 0
  
    # Fill dp[] using above recursive formula 
    for i in range(W + 1): 
        for j in range(n): 
            if (wt[j] <= i): 
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j]) 
  
    return dp[W]


if __name__ == "__main__":
    bunqty = [20,19]
    buncost = [24,20]
    weight = 50
    print(unboundedKnapsack(weight,bunqty,buncost))