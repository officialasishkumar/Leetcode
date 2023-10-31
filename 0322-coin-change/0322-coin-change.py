class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = 9999999
        n = len(coins)
        dp = {}

        def helper(i, curr):
            if i >= n or curr > amount:
                return inf
            if curr == amount:
                return 0
            if (i,curr) in dp:
                return dp[(i,curr)]
            dp[(i,curr)] = min(1 + helper(i, curr + coins[i]), helper(i+1, curr))
            return dp[(i,curr)]

        ans = helper(0,0)
        if ans == inf:
            return -1
        return ans
        