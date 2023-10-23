class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        n = len(colors)
        for i in range(0,n-1):
            if colors[i] == colors[i+1]:
                time += min(neededTime[i], neededTime[i+1])
                neededTime[i+1] = max(neededTime[i], neededTime[i+1])
        return time