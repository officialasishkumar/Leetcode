class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0 for j in range(m)] for i in range(n)]

        def check(x,y):
            if x<0 or y<0 or x>=n or y>=m:
                return False
            return True

        def dfs(i,j):
            for (x,y) in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
                if check(x,y) and grid[x][y] == 0 and  visited[x][y] == 0:
                    visited[x][y] = 1
                    dfs(x,y)
        
        for i in range(0,n):
            if grid[i][0] == 0 and visited[i][0] == 0:
                dfs(i, 0)
            if grid[i][m-1] == 0 and visited[i][m-1] == 0:
                dfs(i,m-1)

        for j in range(0,m):
            if grid[0][j] == 0 and visited[0][j] == 0:
                dfs(0,j)
            if grid[n-1][j] == 0 and visited[n-1][j] == 0:
                dfs(n-1,j)

        count = 0
        for i in range(1,n-1):
            for j in range(1,m-1):
                if grid[i][j] == 0 and visited[i][j] == 0:
                    dfs(i,j)
                    count += 1
        return count
        