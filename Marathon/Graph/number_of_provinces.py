'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.


Example 1:
Input: isConnected = [
[1,1,0],
[1,1,0],
[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]

https://leetcode.com/problems/number-of-provinces/description/
'''

from collections import defaultdict
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.seen = set()
        self.provinces = 0
        self.m = 0
        self.n = 0
        
    def findCircleNum(self, isConnected):
        m,n = len(isConnected), len(isConnected[0])
        for i in range(m):
            for j in range(n):
                if isConnected[i][j] == 1:
                    self.graph[i + 1].append(j+1)
        
        def dfs(node):
            for neighbor_node in self.graph[node]:
                if neighbor_node not in self.seen:
                    self.seen.add(neighbor_node)
                    dfs(neighbor_node)
                    
        for i in self.graph:
            self.provinces += 1
            dfs(i)
        print(self.provinces)
        print(self.graph)
        
# I tried to use the same method from valid tree and number of islands. It didn't work.
s = Solution()
# s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])


# using the exact method without modification using defaultdict
# That didn't work out as it is not grid like number of islands.

class Solution_1:
  
    def findCircleNum(self, isConnected):
        m,n = len(isConnected), len(isConnected[0])        
        provinces = 0
        seen = set()
        def dfs(i,j):
            if (i,j) in seen:
                return
            if i < 0 or i >= m or j < 0 or j >=n or isConnected[i][j] != 1:
               return
            seen.add((i,j))
            isConnected[i][j] = 0
            dfs(i,j + 1)
            dfs(i,j - 1)
            dfs(i + 1,j)
            dfs(i - 1,j)
            
        for i in range(m):
            for j in range(n):
                if isConnected[i][j] == 1:
                    provinces += 1
                    dfs(j,j)
                    

        return provinces
        
   
s = Solution_1()
print(s.findCircleNum([
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,1,1]
]))


# This will work.
def findCircleNum(isConnected):
    provinces = 0
    n = len(isConnected)
    seen = set()
    def dfs(i):
        seen.add(i)
        
        for j in range(n):
            if isConnected[i][j] == 1 and j not in seen:
                dfs(j)
        return
    
    for i in range(n):
        if i not in seen:
            provinces += 1
            dfs(i)
    
    return provinces
print(findCircleNum([
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 1]
]))  # Output: 1