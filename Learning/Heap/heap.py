# Build heap without using heapq.
# Time O(N Log N), but if we use heapify we will get O(N)
import heapq

C = [-5, 4, 2, 1, 7, 0, 3]

# This is Time O(N log N) and Space O(N)
heap = []
for i in C:
    heapq.heappush(heap, i)

# This is Time O(N) and Space O(1)
# heapify method internally uses the Floyd’s algorithm to build the heap bottom-up.
heapq.heapify(C)
print(C)
