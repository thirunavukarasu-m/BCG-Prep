'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"

Output: true

Example 2:
Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

https://leetcode.com/problems/valid-anagram/description/
'''

def is_anagram_1(s, t):
    return sorted(s) == sorted(t)
    
def is_anagram_2(s, t):
    if len(s) != len(t):
        return False
        
    anagram_dict_1 = {}
    anagram_dict_2 = {}
    
    
    for i in s:
        if i in anagram_dict_1:
            anagram_dict_1[i] += 1
        else:
            anagram_dict_1[i] = 0
        
    for i in t:
        if i in anagram_dict_2:
            anagram_dict_2[i] += 1
        else:
            anagram_dict_2[i] = 0
            
    return anagram_dict_1 == anagram_dict_2