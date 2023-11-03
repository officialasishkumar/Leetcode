class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        dp = {}

        def helper(i,buy):
            if i >= n:
                return 0
            if (i,buy) in dp:
                return dp[(i,buy)]
            if buy != -1 and prices[i] > prices[buy]:
                dp[(i,buy)] = max(helper(i+1,buy), prices[i] - prices[buy] + helper(i+2,-1))
            else:
                dp[(i,buy)] = helper(i+1, i)
            return dp[(i,buy)]
        
        return helper(0,-1)