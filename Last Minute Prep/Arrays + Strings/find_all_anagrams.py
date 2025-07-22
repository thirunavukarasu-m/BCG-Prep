'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
'''

def find_all_anagrams(s,t):
    if len(s) < len(t):
        return []
    
    s_dict = {}
    t_dict = {}
    left = 0
    for i in range(len(t)):
        t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
    
    result = [0] if t_dict == s_dict else []
    
    for right in range(len(t), len(s)):
        s_dict[s[right]] = 1 + s_dict.get(s[right], 0)
        s_dict[s[left]] -= 1
        
        if s_dict[s[left]] == 0:
            s_dict.pop(s[left])
        left += 1
        
        if t_dict == s_dict:
            result.append(left)
    
    return result


s = "abab"
t = "ab"
print(find_all_anagrams(s,t))