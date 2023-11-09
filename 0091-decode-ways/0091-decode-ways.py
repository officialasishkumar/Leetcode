class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        dp = [-1]*(n+1)
        dp[n] = 1

        for i in range(n-1,-1,-1):
            if s[i] == "0":
                dp[i] = 0
            elif i < n-1 and int(s[i:i+2]) <= 26:
                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]
        
        return dp[0]


        