# From http://bookshadow.com/weblog/2015/12/27/leetcode-coin-change/
import math

def coinChange(coins, total):
    dp = [math.inf for i in range(total+1)]
    results = [-1 for i in range(total+1)]
    
    for c in range(len(coins)):
        for i in range(1, total):
            if i >= coins[c]:
                if dp[i - coins[c]] + 1 < dp[i]:
                    dp[i] = 1 + dp[i - coins[c]]
                    results[i] = c

    print(dp)
coinChange([3, 2, 4], 6)