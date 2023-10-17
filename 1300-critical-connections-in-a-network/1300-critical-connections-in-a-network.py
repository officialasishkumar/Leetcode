class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        adj = defaultdict(lambda:[])
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)

        time = [0 for i in range(n)]
        low = [0 for i in range(n)]
        visited = [0 for i in range(n)]
        self.time = 1

        def dfs(node, parent):
            visited[node] = 1
            time[node] = self.time
            low[node] = self.time
            self.time += 1
            for nextNode in adj[node]:
                if nextNode != parent:
                    if visited[nextNode] == 0:
                        dfs(nextNode, node)
                    low[node] = min(low[node], low[nextNode])
        
        dfs(0, None)

        critical = []
        for u,v in connections:
            if low[u]>time[v] or low[v]>time[u]:
                critical.append([u,v])
        return critical
