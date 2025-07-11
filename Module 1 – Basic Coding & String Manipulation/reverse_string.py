'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.


Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.


https://leetcode.com/problems/reverse-string/description/
'''
# This should work, but the leetcode is not accepting this.
def reverse_string_1(s):
    s = s[::-1]
    return s
    
print(reverse_string_1(["h","e","l","l","o"]))


def reverse_string_2(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return s
    
print(reverse_string_2(["h","e","l","l","o"]))
