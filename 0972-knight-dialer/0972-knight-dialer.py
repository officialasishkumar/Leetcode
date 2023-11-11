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

        dp = {}

        def helper(curr, moves):
            if moves == 1:
                return 1
            if (curr,moves) in dp:
                return dp[(curr,moves)]
            ans = 0
            for val in adj[curr]:
                ans += helper(val, moves-1)
            dp[(curr,moves)] = ans
            return ans
        
        result = 0
        for start in range(0,10):
            result += helper(start, n)
        return result % ((10**9) + 7)