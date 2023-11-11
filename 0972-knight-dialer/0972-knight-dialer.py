class Solution:
    def knightDialer(self, n: int) -> int:
        numbers = [0 for i in range(10)]
        adj = {
            1:[6,8], 
            2:[7,9],
            3:[4,8],
            4:[3,9,0],
            5:[],
            6:[1,7,0],
            7:[2,6],
            8:[1,3],
            9:[4,2],
            0:[6,4]
            }

        dp = [[-1 for j in range(10)] for i in range(n)]

        for curr in range(10):
            dp[0][curr] = 1

        for moves in range(1,n):
            for curr in range(10):
                ans = 0
                for k in adj[curr]:
                    ans += dp[moves-1][k]
                dp[moves][curr] = ans
        
        result = 0 
        for curr in range(10):
            result += dp[n-1][curr]

        return result % ((10**9) + 7)