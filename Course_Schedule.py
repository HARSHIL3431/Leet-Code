from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        visit = [0] * numCourses
        
        def dfs(course):
            if visit[course] == 1:
                return False
            if visit[course] == 2:
                return True
            
            visit[course] = 1
            
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            visit[course] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True