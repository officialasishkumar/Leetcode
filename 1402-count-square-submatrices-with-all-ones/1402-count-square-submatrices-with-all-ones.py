class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [[-1 for j in range(m)] for i in range(n)]
        self.count = 0

        def helper(i,j):
            if i >= n or j >= m or matrix[i][j] == 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            side_length = 1 + min(min(helper(i+1,j), helper(i,j+1)), helper(i+1,j+1))
            self.count += side_length
            dp[i][j] = side_length
            return side_length

        for i in range(0,n):
            for j in range(0,m):
                if matrix[i][j] == 1 and dp[i][j] == -1:
                    helper(i,j)
        
        return self.count
        