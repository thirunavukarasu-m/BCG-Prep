'''
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1
 

Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000

https://leetcode.com/problems/last-stone-weight/description/

'''
import heapq

# This didn't work cause I forgot to negate the weight difference and while returning I have to again apply negation.
def last_stone_weight_1(stones):
    if len(stones) == 1:
        return stones[0]
    stones = [ -stone for stone in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        y = -heapq.heappop(stones)
        x = -heapq.heappop(stones)
        
        if x != y:
            remaining_weight = y - x
            heapq.heappush(stones, remaining_weight)
        
    return stones[0] if stones else 0
    
    
stones = [3,7,2]
print(last_stone_weight_1(stones))

# This will work.
def last_stone_weight_2(stones):
    if len(stones) == 1:
        return stones[0]
    stones = [ -stone for stone in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        y = -heapq.heappop(stones)
        x = -heapq.heappop(stones)
        
        if x != y:
            remaining_weight = y - x    
            heapq.heappush(stones, -remaining_weight)
        
    return -stones[0] if stones else 0
    
stones = [3,7,2]
print(last_stone_weight_2(stones))