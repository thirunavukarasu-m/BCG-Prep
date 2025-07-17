from collections import defaultdict

def graph_valid_tree(n, edges):
    seen = set()
    UNVISITED, VISITING, VISITED = 0, 1, 2
    states = [UNVISITED] * n
    cache = defaultdict(list)
    for i,j in edges:
        cache[i].append(j)
        cache[j].append(i)
        
    def dfs(node, parent):
        state = states[node]
        if state == VISITED:
            return True
        elif state == VISITING:
            return False
        
        states[node] = VISITING
        seen.add(node)
            
        for nei in cache[node]:
            if nei == parent:
                continue
            if not dfs(nei, node):
                return False
            
        states[node] = VISITED
        return True
        

    if not dfs(0, -1):
        return False
    print(states)
    return len(seen) == n
    
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
n = 5
print(graph_valid_tree(n,edges))