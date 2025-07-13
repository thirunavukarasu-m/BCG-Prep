'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''

# This will work but it takes O(N^2), too slow.
def daily_temperatures_1(arr):
    if not arr:
        return []
    
    n = len(arr)
    result = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                result[i] = (j - i)
                break
    
    return result
    
print(daily_temperatures_1([89,62,70,58,47,47,46,76,100,70]))

# This doesn't work
def daily_temperatures_2(arr):
    result = [0] * len(arr)
    stack = [] # pair of [temp, index] to calculate the days
    
    for index, temp in enumerate(arr):
        if not stack:
            stack.append([temp, index])
            continue
        
        if stack[-1][0] > temp:
            stack.append([temp, index])
            continue
        else:
            while True:
                if stack[-1][0] > temp:
                    break
                popped = stack.pop()
                result[popped[1]] = index - popped[0]
        
        return result
        

print(daily_temperatures_2([89,62,70,58,47,47,46,76,100,70]))


# This works
def daily_temperatures_3(arr):
    result = [0] * len(arr)
    stack = []
    
    for index, temp in enumerate(arr):
        while stack and stack[-1][0] < temp:
            stackTemp, stackIndex = stack.pop()
            result[stackIndex] = index - stackIndex
        stack.append([temp, index])
        
    return result
    
print(daily_temperatures_3([89,62,70,58,47,47,46,76,100,70]))
