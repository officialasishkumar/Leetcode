class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        dp = [-1]*n

        def helper(i):
            if i >= n:
                return 1
            if s[i] == "0":
                return 0
            if dp[i] != -1:
                return dp[i]
            if i < n-1 and int(s[i:i+2]) <= 26:
                dp[i] = helper(i+1) + helper(i+2)
            else:
                dp[i] = helper(i+1)
            return dp[i]
        
        return helper(0)


        