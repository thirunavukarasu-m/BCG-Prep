# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Find the left height and right height, add them and they will be the diameter of the current node.
class Solution:
    def __init__(self):
        self.max_depth = 0
    def diameterOfBinaryTree(self, root):
        def dfs(root):
            if not root:
                return 0

            left_height = dfs(root.left)
            right_height = dfs(root.right)
            diameter = left_height + right_height
            self.max_depth = max(self.max_depth, diameter)
            
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.max_depth