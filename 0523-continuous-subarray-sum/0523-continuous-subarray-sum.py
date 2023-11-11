class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix={0:-1}
        curr=0
        for i in range(len(nums)):
            curr+=nums[i]
            if curr%k in prefix:
                if prefix[curr%k]<=i-2:
                    return True
            else:
                prefix[curr%k]=i
        return False