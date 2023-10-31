class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = 9999999
        n = len(coins)
        dp = [-1 for i in range(amount+1)]
        dp[0] = 0

        def helper(rem):
            if rem < 0:
                return inf
            if dp[rem] != -1:
                return dp[rem]
            val = inf
            for coin in coins:
                val = min(val, 1 + helper(rem - coin))
            dp[rem] = val
            return val

        ans = helper(amount)
        if ans == inf:
            return -1
        return ans
        