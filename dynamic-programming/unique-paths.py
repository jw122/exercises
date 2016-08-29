class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 and n == 1:
            dp = [[1]]
        
        elif m == 1 and n > 1:
            dp = [[1 for i in range(n)]]
        elif m > 1 and n == 1:
            dp = [[1] for i in range(m)]
        else:
            dp = [[0 for i in range(n)] for j in range(m)]
            
            dp[0][0] = 1
            
            for i in range(1, m):
                dp[i][0] = 1
            for j in range(1, n):
                dp[0][j] = 1
            for i in range(1, m):
                for j in range(1, n):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]