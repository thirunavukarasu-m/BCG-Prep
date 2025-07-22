'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.


https://leetcode.com/problems/permutations/
'''

def permutations(nums):
    if not nums:
        return []
    
    n = len(nums)
    result, solution = [], []
    
    def backtrack():
        if len(solution) == n:
            result.append(solution[:])
            return
        for x in nums:
            if x not in solution:
                solution.append(x)
                backtrack()
                solution.pop()
    backtrack()
    return result

nums = [1,2,3]
print(permutations(nums))