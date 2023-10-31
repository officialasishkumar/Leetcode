class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        target = 0
        for i in nums:
            target += i
        if target % 2 == 1:
            return False
        target = target // 2  

        dp = [[False for i in range(target+1)] for j in range(n)]

        for i in range(n):
            dp[i][0] = True

        for i in range(1,n):
            for rem in range(1,target+1):
                if nums[i] <= rem:
                    dp[i][rem] = dp[i-1][rem] or dp[i-1][rem-nums[i]]
                else:
                    dp[i][rem] = dp[i-1][rem]
        
        return dp[n-1][target]