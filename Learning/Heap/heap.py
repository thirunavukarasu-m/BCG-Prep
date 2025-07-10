# Build heap without using heapq.
# Time O(N Log N), but if we use heapify we will get O(N)
import heapq

C = [-5, 4, 2, 1, 7, 0, 3]

heap = []

for i in C:
    heapq.heappush(heap, i)
    
print(heap)
