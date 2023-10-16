class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        leftProd = 1
        leftMax = -9999999999
        rightProd = 1
        rightMax = -9999999999

        for i in range(0,n):
            leftProd *= nums[i]
            leftMax = max(leftProd, leftMax)
            rightProd *= nums[n-i-1]
            rightMax = max(rightProd, rightMax)

            if leftProd == 0:
                leftProd = 1
            if rightProd == 0:
                rightProd = 1
        
        return max(leftMax, rightMax)