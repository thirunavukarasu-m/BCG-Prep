'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0

https://leetcode.com/problems/add-digits/description/
'''

# This solution is of O(log n) time complexity.
def add_digits_1(number):
    if number == 0 or len(str(number)) == 1:
        return number
    while len(str(number)) > 1:
        buffer = 0
        for i in str(number):
            buffer += int(i)
        number = buffer
    return number
    
print(add_digits_1(100))

# This happens at O(1) using something called a digital root.
def add_digits_2(number):
    if number == 0:
        return 0
    return 1 + (number - 1) % 9
    
print(add_digits_2(38))