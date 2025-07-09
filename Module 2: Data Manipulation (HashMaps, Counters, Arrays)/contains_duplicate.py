'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:
Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

https://leetcode.com/problems/contains-duplicate/description/
'''

def contains_duplicate_1(nums):
    print(nums, set(nums))
    if len(set(nums)) == len(nums):
        return False
    return True
    
print(contains_duplicate_1([1,2,3,1]))


def contains_duplicate_2(nums):
    counts_set = set()
    for i in nums:
        if i not in counts_set:
            counts_set.add(i)
        else:
            return True
            
    return False