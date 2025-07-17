# https://leetcode.com/problems/course-schedule/

from collections import defaultdict

def canFinish(numCourses, prerequisites):
    cache = defaultdict(list)
    
    UNVISITED, VISITING, VISITED = 0, 1, 2
    visits = [UNVISITED] * numCourses

    for i,j in prerequisites:
        cache[i].append(j)
        visits[i] = UNVISITED
        
    # print(visits)
    # return
    def dfs(node):
        state = visits[node]
        if state == VISITING:
            return False
        elif state == VISITED:
            return True
        
        visits[node] = VISITING

        for nei in cache[node]:
            if not dfs(nei):
                return False

        visits[node] = VISITED
        return True

    
    for i in range(numCourses):
        if not dfs(i):
            return False

    return True
    
    
print(canFinish(2, [[1,0]]))