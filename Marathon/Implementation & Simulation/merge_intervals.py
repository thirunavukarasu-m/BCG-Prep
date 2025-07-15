'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

https://leetcode.com/problems/merge-intervals/
'''

def merge_intervals(arr):
    stack = []
    arr.sort()
    for i,j in arr:
        if not stack:
            stack.append([i,j])
            continue
        if stack[-1][1] >= i:
            # Instead of this, we can directly overwrite the data in last place.
            # popped = stack.pop()
            # stack.append([min(popped[0], i), max(popped[1],j)])
            stack[-1] = [min(stack[-1][0], i), max(stack[-1][1], j)]
        else:
            stack.append([i,j])
    
    print(stack)
arr = [[2,3],[1,4]]
arr = [[8,10],[15,18], [1,3],[2,6]]
merge_intervals(arr)