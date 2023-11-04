class Solution:
    def twoEggDrop(self, n: int) -> int:
        
        if n <= 2:
            return n

        inf = 999999999
        dp = [inf for i in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i] = min(dp[i], 1 + max(dp[i-j], j-1))

        print(dp)
        return dp[n]