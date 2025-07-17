def invert_binary_tree(root):
    if not root:
        return
    
    root.right, root.left = root.left, root.right
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right