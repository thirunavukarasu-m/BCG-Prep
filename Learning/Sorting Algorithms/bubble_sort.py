# Time : O(N^2)
# Space O(1) In place swap

A = [9,8,7,76,6,5,4,3,2,21,4,4,6,7,8]

for i in range(len(A)):
    for j in range(1, len(A) - i):
        if A[j-1] > A[j]:
            A[j-1], A[j] = A[j], A[j-1]
            
print(A)