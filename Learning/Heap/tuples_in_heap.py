from collections import Counter
import heapq
A = [5,4,3,5,4,3,5,5,4]

# Creates a dictionary with the repeatation counts.
counter = Counter(A)
print(counter)
# Counter({5: 4, 4: 3, 3: 2})

heap = []
for key, value in counter.items():
    print(key, value)
    heapq.heappush(heap, (value, key))

print(heap)
# [(2, 3), (4, 5), (3, 4)]

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))

    