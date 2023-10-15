class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:
            return True
            
        adj = defaultdict(lambda:[])
        for i in range(0,len(edges)):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])

        # BFS TRAVERSAL - While loop, Queue - O(V+E)

        queue = [source]
        visited = [0]*n
        visited[source] = 1

        while queue: 
            nextLevel = []
            for node in queue:
                for nextNode in adj[node]:
                    if visited[nextNode] == 0:
                        if nextNode == destination:
                            return True
                        nextLevel.append(nextNode)
                        visited[nextNode] = 1
            queue = nextLevel

        return False

        # DFS TRAVERSAL - Recursion - O(V+E)

        def dfs(node):
            for nextNode in adj[node]:
                if visited[nextNode] == 0:
                    if nextNode == destination:
                        return True
                    visited[nextNode] = 1
                    if dfs(nextNode):
                        return True
            return False

        return dfs(source)
            

