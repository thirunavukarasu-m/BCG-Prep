# Not sorted, doesn't satisfy the  heap property.
import heapq
A = [-4, 3, 1,0, 2, 5, 10, 8, 12, 9]

# We don't have a method to create Max Heap. We can negate the values and use the Min Heap to create Max Heap.


for i in range(len(A)):
    A[i] = -A[i]

heapq.heapify(A)

print(A)

print("Largest Number - ", -heapq.heappop(A))


# Heap Push, Give the negated number to perform correctly.
heapq.heappush(A, -7)
# This pushes 7 into Max heap.
# 


# Peek
# O(1)
print(A[0])