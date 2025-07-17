"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        cache = {}
        start = node
        def dfs(node):
            if not node:
                return
            if node not in cache:
                cache[node] = Node(node.val)
            else:
                return
            for i in node.neighbors:
                dfs(i)
        
        dfs(node)
        for old,new in cache.items():
            for nei in old.neighbors:
                new.neighbors.append(cache[nei])
        
        return cache[start]