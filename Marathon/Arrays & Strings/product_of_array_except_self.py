'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

https://leetcode.com/problems/product-of-array-except-self/description/
'''

# The brute force solution would take O(N^2), two for loops where i == j skip.

# Too slow.
def product_of_array_except_self_brute(arr):
    n = len(arr)
    ans = [0]*n
    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= arr[j]
        ans[i] = prod
    return ans
    
# print(product_of_array_except_self_brute([0,4,0]))

# This almost solves all the use cases. But fails at [0,4,0].
def product_of_array_except_self(arr):
    ans = [0] * len(arr)
    prod = None
    zero_indexes = set()
    for index, value in enumerate(arr):
        if value == 0:
            zero_indexes.add(index)
        else:
            if prod is not None:
                prod *= value
            else:
                prod = value
    print(prod)
    if zero_indexes:
        for i in zero_indexes:
            ans[i] = prod
        return ans
    else:
        for index, value in enumerate(arr):
            ans[index] = prod//value
            
    
    return ans
    
    
data = [0,4,0]
# print(product_of_array_except_self(data))

# This works.
def product_of_array_except_self_l_r(arr):
    n = len(arr)
    ans = [0] * n
    L = [1] * n
    R = [1] * n
    
    for index in range(1,n):
        L[index] = L[index - 1] * arr[index - 1]
        
    for index in range(n - 2, -1, -1):
        R[index] = arr[index + 1] * R[index + 1] 
        
    for index in range(n):
        ans[index] = L[index] * R[index]
    return ans
print(product_of_array_except_self_l_r([1,2,3,4]))
