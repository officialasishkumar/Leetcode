class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        inf = 9999999
        dp = {}

        def helper(i,j):
            if j-i <= 1:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            cost = inf
            for cut in cuts:
                if cut > i and cut < j:
                    currCost = j-i + helper(i,cut) + helper(cut,j)
                    cost = min(cost, currCost)
            if cost == inf:
                dp[(i,j)] = 0
            else:
                dp[(i,j)] = cost
            return dp[(i,j)]
        
        return helper(0,n)