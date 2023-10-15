class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r=len(heights)
        c=len(heights[0])
        efforts = [[-1 for i in range(c)] for j in range(r)]
        efforts[0][0] = 0

        def check(i,j):
            if i < 0 or j < 0 or i >= r or j >= c:
                return False
            return True

        q = [(0,0)]
        while q:
            temp = []
            for (i,j) in q:
                for (x,y) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if check(x,y):
                        if efforts[x][y] == -1 or efforts[x][y] > max(efforts[i][j], abs(heights[x][y]-heights[i][j])):
                            temp.append((x,y))
                            efforts[x][y] = max(efforts[i][j], abs(heights[x][y] - heights[i][j]))
            q = temp
        
        return efforts[r-1][c-1]