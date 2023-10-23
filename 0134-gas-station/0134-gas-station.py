class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas, total_dist = 0, 0
        n = len(gas)
        for i in range(0,n):
            total_gas += gas[i]
            total_dist += cost[i]
        if total_gas < total_dist:
            return -1

        start = 0
        curr_gas = 0
        for i in range(0,n):
            curr_gas += gas[i] - cost[i]
            if curr_gas < 0:
                start = i+1
                curr_gas = 0
        return start