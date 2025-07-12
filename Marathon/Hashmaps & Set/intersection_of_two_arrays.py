'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


https://leetcode.com/problems/intersection-of-two-arrays/description/
'''

# Both the implementation takes the same time and space complexity O(n+m) where n is len of arr_1 and m is arr_2.
def intersection_of_two_arrays_1(arr_1, arr_2):
    cache = set()
    seen = set()
    result = []
    for i in arr_1:
        if i not in cache:
            cache.add(i)
        
    for j in arr_2:
        if j in cache and j not in seen:
            seen.add(j)
            result.append(j)
    
    return result
    
nums1, nums2 = [1,2,2,1], [2,2]
print(intersection_of_two_arrays_1(nums1, nums2))


def intersection_of_two_arrays_2(arr_1, arr_2):
    return list(set(arr_1) & set(arr_2))
print(intersection_of_two_arrays_2(nums1, nums2))
