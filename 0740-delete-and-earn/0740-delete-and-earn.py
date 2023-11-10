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

        dp = [-1 for i in range(n+1)]
        dp[n] = 0
        dp[n-1] = arr[n-1] * count[arr[n-1]]

        for i in range(n-2, -1, -1):
            if arr[i+1] - arr[i] == 1:
                dp[i] = max(dp[i+1], (arr[i]*count[arr[i]]) + dp[i+2])
            else:
                dp[i] = max(dp[i+1], (arr[i]*count[arr[i]]) + dp[i+1])

        return dp[0]
        