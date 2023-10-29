class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [-1 for i in range(n)]
        dp[0] = 1

        longestSub = 1
        for i in range(1,n):
            curr = 1
            for j in range(0,i):
                if nums[i] > nums[j]:
                    curr = max(curr, dp[j]+1)
            dp[i] = curr
            longestSub = max(longestSub, curr)
        
        return longestSub
