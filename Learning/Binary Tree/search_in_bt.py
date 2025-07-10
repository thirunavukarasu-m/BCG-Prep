class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left
        
    def __str__(self):
        return str(self.val)
        
#       1
#   2       3
# 4   5   10

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(10)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

# O(N) Time and Space
def search_iterative(node, target):
    
    stk = [node]
    while stk:
        node = stk.pop()
        if node.val == target:
            return True
        
        if node.right:
            stk.append(node.right)
        
        if node.left:
            stk.append(node.left)
            
    return False
            
# print(search_iterative(a, 5))

# The reason we don't have an if condition is, if we use it the unwanted call stacks will be created. This or condition will check if either one is True and return it.
def search_recursive(node, target):
    if not node:
        return False
    print(node.val, node.val == target)
    if node.val == target:
        return True

    return search_recursive(node.right, target) or search_recursive(node.left, target)
        
print(search_recursive(a, 5))
