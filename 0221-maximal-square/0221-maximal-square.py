class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        maxVal = 0

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i+1][j], min(dp[i][j+1], dp[i+1][j+1]))
                    maxVal = max(maxVal, dp[i][j])
                    
        return maxVal ** 2
            