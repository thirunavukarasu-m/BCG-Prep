'''
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
 

Follow up: Could you find an O(nums1.length + nums2.length) solution?

https://leetcode.com/problems/next-greater-element-i/description/
'''

# This works, but very slow O(N^2).
def next_greater_element_I_1(nums1, nums2):
    result = [-1] * len(nums1)
    seen = set()
    can_check = False
    for i_index, i in enumerate(nums1):
        seen.add(i)
        for j_index, j in enumerate(nums2):
            if j in seen:
                can_check = True
            if can_check and j > i:
                result[i_index] = nums2[j_index] 
                can_check = False
                seen = set()
                break
        
        can_check = False
        seen = set()

    return result
    
nums1 = [4,1,2]
nums2 = [1,2,3,4]
# print(next_greater_element_I_1(nums1, nums2))

# The same solution but with dictionary.
# This is much faster than the previous solution as it cuts down the unwanted loops for values not in nums1.
def next_greater_element_I_2(nums1, nums2):
    mapped_nums1 = {n:i for i,n in enumerate(nums1)}
    
    result = [-1]* len(nums1)
    
    for i_index, i_value in enumerate(nums2):
        if i_value not in mapped_nums1:
            continue
        for j_index in range(i_index + 1, len(nums2)):
            if nums2[j_index] > i_value:
                result[mapped_nums1[i_value]] = nums2[j_index]
                break
    return result
    

        
print(next_greater_element_I_2(nums1, nums2))


# This is much faster than the previous solutions.
def next_greater_element_I_3(num1, nums2):
    cache = {n:i for i,n in enumerate(nums1)}
    stack = []
    result = [-1] * len(nums1)
    for i in range(len(nums2)):
        # nums1 = [4,1,2]
        # nums2 = [1,2,3,4]

        while stack and nums2[i] > stack[-1]:
            popped = stack.pop()
            result[cache[popped]] = nums2[i]
            
        # It is crucial that we have the if after while. if the condition is placed before while, then we are adding value before checking the top element and popping condition.
        # if we want to have the condition before we would still need a while loop to check if stack and greater than top element.
        if nums2[i] in cache:
            stack.append(nums2[i])
    return result
    
print(next_greater_element_I_3(nums1, nums2))

    
