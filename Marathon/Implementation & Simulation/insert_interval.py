'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105

https://leetcode.com/problems/insert-interval/
'''

# This doesn't work.
def insert_interval_1(arr, new_interval):
    stack = []
    # arr.sort()
    check_for_new_interval = True
    for i,j in arr:
        if not stack:
            if new_interval[0] < i:
                stack.append(new_interval)
                check_for_new_interval = False
                continue
            else:
                print("here")
                stack.append([i,j])
                continue
        
        print(stack[-1][1],check_for_new_interval)
        if check_for_new_interval:
            print(1111, stack)
            
            if stack[-1][1] >= new_interval[0]:
                print('1123123')
                popped = stack.pop()
                stack.append([min(popped[0], new_interval[0]), max(popped[1],new_interval[1])])
                check_for_new_interval = False
            if new_interval[0] < i:
                stack.append(new_interval)
                check_for_new_interval = False
            else:
                stack.append([i,j])
            if stack[-1][1] >= i:
                popped = stack.pop()
                stack.append([min(popped[0], i), max(popped[1],j)])
        else:
            if stack[-1][1] >= i:
                popped = stack.pop()
                stack.append([min(popped[0], i), max(popped[1],j)])
    print(stack)
insert_interval_1([[1,2],[3,5]], [4,8])

def insert_interval_2(arr, new_interval):
    result = []
    
    for i in range(len(arr)):
        if arr[i][0] > new_interval[1]:
            result.append(new_interval)
            return result + arr[i:]
        elif new_interval[0] > arr[i][1]:
            result.append(arr[i])
        else:
            new_interval = [min(new_interval[0],arr[i][0]), max(new_interval[1],arr[i][1])]
            
    result.append(new_interval)
    return result
        

print(insert_interval_2([[1,3],[6,9]], [2,5]))
