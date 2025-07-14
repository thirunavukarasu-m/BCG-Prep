'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"

Output: true

Example 2:
Input: s = "()[]{}"

Output: true

Example 3:
Input: s = "(]"

Output: false

Example 4:
Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

https://leetcode.com/problems/valid-parentheses/description/
'''

def valid_parenthesis(s):
    stk = []
    cache = {')':"(", "]":'[','}':'{'}
    
    for i in s:
        if i not in cache:
            stk.append(i)
        else:
            popped = stk.pop()
            if cache[i] != popped:
                return False
            
            
    return True if not stk else False
        
print(valid_parenthesis("("))


def valid_parenthesis_2(s):
    if len(s) < 2:
        return False
    stk = []
    cache = {')' : '(', '}': '{', ']': '['}
    i = 0

    while i < len(s):
        if s[i] not in cache:
          stk.append(s[i])
        else:
            if (cache[s[i]] and not stk) or (cache[s[i]] != stk.pop()):
                return False
        i += 1
        
    return True if not stk else False
    
print(valid_parenthesis_2(""))