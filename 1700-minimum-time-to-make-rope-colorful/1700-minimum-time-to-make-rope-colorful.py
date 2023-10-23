class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        n = len(colors)
        prev = 0
        next = 1
        while next < n:
            if colors[prev] == colors[next]:
                print(prev,next)
                if neededTime[prev] < neededTime[next]:
                    time += neededTime[prev]
                    prev = next
                else:
                    time += neededTime[next]
            else:
                prev = next
            next += 1
        return time