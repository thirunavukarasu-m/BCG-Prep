import heapq
from collections import Counter
def top_k_frequent(arr, k):
    if not arr:
        return []
    result = []
    counter = Counter(arr)
    count_to_vals = []
    for val, count in counter.items():
        count_to_vals.append([-count, val])
    
    heapq.heapify(count_to_vals)
    for i in range(k):
        if count_to_vals:
            result.append(heapq.heappop(count_to_vals)[1])
        else:
            return result
    return result
nums = [1]
k = 2

top_k_frequent(nums,k)
