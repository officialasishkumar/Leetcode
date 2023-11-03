class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[[-1 for i in range(0,2)] for j in range(0,2)] for k in range(0,n)]

        def helper(i, buy, limit):
            if i >= n or limit == 0:
                return 0
            if dp[i][buy][limit-1] != -1:
                return dp[i][buy][limit-1]
            if buy:
                trade = prices[i] + helper(i+1, 0, limit-1)
            else:
                trade = -prices[i] + helper(i+1, 1, limit)
            wait = helper(i+1, buy, limit)
            dp[i][buy][limit-1] = max(wait, trade)
            return dp[i][buy][limit-1]
        
        return helper(0,0,2)