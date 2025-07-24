'''
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth

https://leetcode.com/problems/text-justification/description/
'''

def fullJustify(words, maxWidth):
    result, line, length = [], [], 0
    i = 0
    
    while i < len(words):
        if length + len(line) + len(words[i]) > maxWidth:
            extra_spaces = maxWidth - length
            common_spaces = extra_spaces // max(1, len(line) - 1)
            remainder_spaces = extra_spaces % max(1, len(line) - 1)
            
            if len(line) == 1:
                line[0] += " " * extra_spaces
            else:
                for j in range(len(line) - 1):
                    line[j] += ' '* common_spaces
                    if remainder_spaces:
                        line[j] += ' '
                        remainder_spaces -= 1
            result.append(''.join(line))
            line, length = [], 0
        
        line.append(words[i])
        length += len(words[i])
        i += 1
        
    last_line = ' '.join(line)
    remaining_space = maxWidth - len(last_line)
    result.append(last_line + ' '* remaining_space)
    return result