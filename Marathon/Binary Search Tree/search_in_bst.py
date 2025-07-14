'''
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]


Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107

https://leetcode.com/problems/search-in-a-binary-search-tree/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# It seems we don't need the dfs, returning the root will be enough as it has the ref of subtree which belongs to it.
class Solution:
    # def __init__(self):
    #     self.result = []
        
    # def dfs(self, node):
    #     if not node:
    #         return
        
    #     self.result.append(node)
    #     self.dfs(node.left)
    #     self.dfs(node.right)
        
    def searchBST(self, root, val):
        if not root:
            return None
        if root.val == val:
            # So this is not needed.
            # self.dfs(root) 
            # return self.result
            return root # This is enough.
            
        if root.val < val:
            self.searchBST(root.right, val)
        else:
            self.searchBST(root.left, val)
        
        return []