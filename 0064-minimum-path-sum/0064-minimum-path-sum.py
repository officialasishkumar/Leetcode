class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        inf = 9999999

        dp = [[-1 for i in range(m)] for j in range(n)]
        dp[n-1][m-1] = grid[n-1][m-1]
        
        def helper(i,j):
            if i >= n or j >= m:
                return inf
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = grid[i][j] + min(helper(i+1, j), helper(i, j+1))
            return dp[i][j]
        
        return helper(0,0)
        