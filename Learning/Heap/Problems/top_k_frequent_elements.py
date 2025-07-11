'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
input_list = [1,1,1,1,2,3,5,6,7,8,8,9,9,9]
from collections import defaultdict, Counter
import heapq

# if counts checks if the heap has any values cause there is a possiblity where k may be greater than the total length.
# In leetcode this is much faster.
def top_k_1(input_list, k):
    counter = Counter(input_list)
    cntsToVals = defaultdict(list)
    
    for val, count in counter.items():
        cntsToVals[count].append(val)
    
    counts = [-cnt for cnt in cntsToVals.keys()]
    heapq.heapify(counts)
    
    result = []
    for i in range(k):
        if counts:
            popped = -heapq.heappop(counts)
        else:
            return result
        for j in range(len(cntsToVals[popped])):
            if len(result) == k:
                return result
            result.append(cntsToVals[popped][j])
    
    return result
print(top_k_1(input_list, 6))


# In leetcode this is a bit slow.
def top_k_2(input_list, k):
    counter = Counter(input_list)
    cntsToVals = defaultdict(list)
    
    for val, count in counter.items():
        cntsToVals[count].append(val)
    
    counts = [-cnt for cnt in cntsToVals.keys()]
    heapq.heapify(counts)
    
    result = []
    for i in range(len(counts)):
        popped = -heapq.heappop(counts)

        for num in cntsToVals[popped]:
            if len(result) == k:
                return result
            result.append(num)
    
    return result
print(top_k_2(input_list, 6))