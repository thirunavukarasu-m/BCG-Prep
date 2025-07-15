'''
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''

def longest_substring_without_repeatation(s):
    if not s:
        return -1
    
    count = 0
    pointer_one = 0
    seen = set()
    
    for pointer_two, value in enumerate(s):
        while value in seen:
            seen.remove(s[pointer_one])
            pointer_one += 1
        
        seen.add(value)
        count = max(count, (pointer_two - pointer_one) + 1)

    return len(seen)
    
print(longest_substring_without_repeatation('pwwkew'))