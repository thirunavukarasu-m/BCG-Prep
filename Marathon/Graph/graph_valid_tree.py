'''
Graph Valid Tree
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:
Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true

Example 2:
Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

Output:
false
Note:

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2

'''


from collections import defaultdict

class Solution:
    
    def validTree(self, n, edges):
        if not n:
            return True
            
        graph = defaultdict(list)
        seen = set()
        
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        def dfs(node, prev):
            if node in seen:
                return False
            seen.add(node)
            for neighbor_node in graph[node]:
                if neighbor_node == prev:
                    continue
                
                if not dfs(neighbor_node, node):
                    return False
        
            return True
            
        
        return dfs(0,-1) and n == len(seen)
        
            
s = Solution()
print(s.validTree(5,[[0, 1], [0, 2], [0, 3], [1, 4]]))