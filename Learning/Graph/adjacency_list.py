from collections import defaultdict

n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

dd = defaultdict(list)

for i,j in A:
    dd[i].append(j)
    # dd[j].append(i) # Uncomment if we need undirected graph.
    
    
print(dd)

# What is node 3 connected to? Access is easy.
print(dd[3])