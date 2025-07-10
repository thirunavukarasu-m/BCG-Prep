# Array of Edges (Directed) [Start, End]
n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

# Convert Array of Edges -> Adjacency Matrix

M = []
for i in range(len(A)):
    M.append([0]*n)
    
# print(M)

for i,j in A:
    M[i][j] = 1
    # M[j][i] = 1 # If we want it to be undirected.
print(M)
# This would be a symmetric matrix.
