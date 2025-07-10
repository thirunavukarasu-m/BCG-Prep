from collections import defaultdict

n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

dd = defaultdict(list)

for i,j in A:
    dd[i].append(j)
    # dd[j].append(i) # Uncomment if we need undirected graph.
    
print(dict(dd))
# DFS with Recursion - O(V + E) where V is the number of nodes and E is the number of edges.


def dfs_recursive(node):
    print(node)
    for neighbor_node in dd[node]:
        if neighbor_node not in seen_set:
            seen_set.add(neighbor_node)
            dfs_recursive(neighbor_node)    
source = 0
seen_set = set()
seen_set.add(source)
dfs_recursive(source)