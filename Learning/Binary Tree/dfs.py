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

def pre_order_1(node):
    if not node:
        return
    
    print(node)
    pre_order_1(node.left)
    pre_order_1(node.right)


# pre_order_1(a)

def in_order_1(node):
    if not node:
        return
    
    
    in_order_1(node.left)
    print(node)
    in_order_1(node.right)


# in_order_1(a)

def post_order_1(node):
    if not node:
        return
    
    
    post_order_1(node.left)
    post_order_1(node.right)
    print(node)
    
# post_order_1(a)

def iterative_pre_order_1(node):
    if not node:
        return
    stk = [node]
    while stk:
        popped = stk.pop()
        print(popped)
        if popped.right:
            stk.append(popped.right)
        if popped.left:
            stk.append(popped.left)
            

def iterative_post_order_1(node):
    if not node:
        return
    stk_1 = [node]
    stk_2 = []
    while stk_1:
        popped = stk_1.pop()
        stk_2.append(popped)
        if popped.left:
            stk_1.append(popped.left)
        if popped.right:
            stk_1.append(popped.right)
    
    while stk_2:
        popped = stk_2.pop()
        print(popped)
            
# iterative_post_order_1(a)

def iterative_inorder(root):
    stack = []
    current = root

    while stack or current:
        # Reach the leftmost node of current
        while current:
            stack.append(current)
            current = current.left

        # Current is None at this point
        current = stack.pop()
        print(current)  # Visit the node

        # Now, move to right subtree
        current = current.right
        
        
print(iterative_inorder(a))