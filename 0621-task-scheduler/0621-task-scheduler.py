import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        pq = []
        heapq.heapify(pq)
        for task in tasks:
            if task in count:
                count[task] += 1
            else:
                count[task] = 1
        for task in count.keys():
            heapq.heappush(pq,(0,task))
        
        print(pq)
        
        time = 0
        done = 0
        while done < len(tasks):
            t,nextTask = heapq.heappop(pq)
            done += 1
            time = max(time, t) + 1
            count[nextTask] -= 1
            if count[nextTask] > 0:
                heapq.heappush(pq,(t+n+1,nextTask))
        return time