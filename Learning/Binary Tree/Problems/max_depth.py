'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


test = [3,9,20,15,7]
A =  TreeNode(3)
B =  TreeNode(9)
C =  TreeNode(20)
D =  TreeNode(15)
E =  TreeNode(7)

A.left = B
A.right = C
C.right = E
C.left = D


def max_depth(root):
    if not root:
        return 0
        
    left = max_depth(root.left)
    right = max_depth(root.right)
    
    return 1 + max(left, right)

print(max_depth(D))


