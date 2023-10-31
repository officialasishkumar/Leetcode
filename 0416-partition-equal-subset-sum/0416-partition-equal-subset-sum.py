class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        target = 0
        for i in nums:
            target += i
        if target % 2 == 1:
            return False
        target = target // 2  

        dp = {}

        def helper(i, rem):
            if rem == 0:
                return True
            if rem < 0 or i >= n:
                return False
            if (i,rem) in dp:
                return dp[(i,rem)]
            dp[(i,rem)] = helper(i+1, rem-nums[i]) or helper(i+1, rem)
            return dp[(i,rem)]
        
        return helper(0, target)