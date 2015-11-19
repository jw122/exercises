class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        
        dp = [[0]*cols]*rows
        
        dp[0][0] = grid[0][0]
        
        for i in range(1, cols):
            dp[0][i] = dp[0][i-1] + grid[0][i]
            
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            
        for i in range(1, rows):
            for j in range(1, cols):
                if dp[i-1][j] < dp[i][j-1]:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                    
        return dp[rows-1][cols-1]
