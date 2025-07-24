'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

https://leetcode.com/problems/permutations-ii/description/
'''
# This didn't work.
def permutations_(nums):
    if not nums:
        return []

    n = len(nums)
    result, sol = [], []
    s = set()

    def backtrack():
        if len(sol) == n:
            a = tuple(sol)
            if a not in s:
                s.add(a)
                result.append(sol[:])
                return
            

        for x in nums:
            sol.append(x)
            backtrack()
            sol.pop()

    backtrack()
    return result
    
# print(permutations_([1,1,2]))


def permutations_1(nums):
    n = len(nums)
    result, sol = [], []
    
    count = {}
    for i in nums:
        count[i] = 1 + count.get(i, 0)
    
    def backtrack():
        if len(sol) == n:
            result.append(sol[:])
            return
            
        for i in count:
            if count[i] > 0:
                sol.append(i)
                count[i] -= 1
                
                backtrack()
                count[i] += 1
                sol.pop()
    
    backtrack()
    return result
    

print(permutations_1([1,1,2]))
