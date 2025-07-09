'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]

Output: [[""]]

Example 3:
Input: strs = ["a"]

Output: [["a"]]

https://leetcode.com/problems/group-anagrams/description/

'''

def group_anagrams(strs):
    if not strs:
        return []
    
    anagram_dict = {}
    for string in strs:
        sorted_string = ''.join(sorted(string))
        if sorted_string not in anagram_dict:
            anagram_dict[sorted_string] = [string]
        else:
            anagram_dict[sorted_string].append(string)
        
    return list(anagram_dict.values())
strs = ["eat","tea","tan","ate","nat","bat"]

print(group_anagrams(strs))