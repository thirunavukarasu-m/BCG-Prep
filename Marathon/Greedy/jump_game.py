'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105

https://leetcode.com/problems/jump-game/description/
'''

# This is very slow due to recursion.
def jump_game(arr):
    n = len(arr)
    cache = {n-1: True}
    def can_jump(i):
        if i in cache:
            return cache[i]
            
        for jump in range(1, arr[i] + 1): # Cause 0 steps can't be taken.
            if can_jump(i + jump):
                cache[i] = True
                return True
        
        cache[i] = False
        return False
    
    return can_jump(0)
    
print(jump_game([3,2,1,0,4]))


# Greedy approach
def jump_game_greedy(arr):
    n = len(arr)
    target = n - 1
    
    for i in range(n - 1, -1 ,-1):
        if i + arr[i] >= target:
            target = i
    
    return target == 0
    
print(jump_game_greedy([3,2,1,0,4]))
