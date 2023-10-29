class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[-1 for i in range(m)] for j in range(n)]

        def helper(i,j):
            if i>=n or j>=m:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = 1 + helper(i+1, j+1)
            else:
                dp[i][j] = max(helper(i+1,j), helper(i,j+1))
            return dp[i][j]
        
        return helper(0,0)