class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = {}
        for val in nums:
            if val in count:
                count[val] += 1
            else:
                count[val] = 1
        
        arr = [x for x in count.keys()]
        arr.sort()
        n = len(arr)

        dp = [-1 for i in range(n)]

        def helper(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            if i == n-1 or arr[i+1] - arr[i] == 1:
                dp[i] = max(helper(i+1), (arr[i]*count[arr[i]]) + helper(i+2))
            else:
                dp[i] = max(helper(i+1), (arr[i]*count[arr[i]]) + helper(i+1))
            return dp[i]
        
        return helper(0)
        