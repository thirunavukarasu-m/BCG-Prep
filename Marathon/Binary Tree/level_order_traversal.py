# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def inorderTraversal_recursion(root):
    result = []
    def test(root):
        if not root:
            return 
        
        test(root.left)
        result.append(root.val)
        test(root.right)
    test(root)
    return result
    

def inorderTraversal_iterative(root):
    stack = []
    current = root
    result = []
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
            
        current = stack.pop()
        result.append(current.val)
    
        current = current.right
    
    return result