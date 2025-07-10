from collections import defaultdict

n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

dd = defaultdict(list)

for i,j in A:
    dd[i].append(j)
    # dd[j].append(i) # Uncomment if we need undirected graph.
    
print(dict(dd))


# BFS - O(V + E) where V is the number of nodes and E is the number of edges.
from collections import deque


def bfs(node):
    q = deque()
    q.append(node)
    while q:
        popped = q.popleft()
        print(popped)
        
        for neighbor_node in dd[popped]:
            if neighbor_node not in seen:
                seen.add(neighbor_node)
                q.append(neighbor_node)
                


source = 0
seen = set()
seen.add(source)
bfs(source)