class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for i in range(numCourses)]
        req = [[] for i in range(numCourses)]
        available = []

        for i in range(0, len(prerequisites)):
            indegree[prerequisites[i][0]] += 1
            req[prerequisites[i][1]].append(prerequisites[i][0])
        
        for i in range(0, numCourses):
            if indegree[i] == 0:
                available.append(i)
        
        while available:
            temp = []
            for course in available:
                for nextCourse in req[course]:
                    indegree[nextCourse] -= 1
                    if indegree[nextCourse] == 0:
                        temp.append(nextCourse)
            available = temp
        
        for i in range(0, numCourses):
            if indegree[i] > 0:
                return False
        return True