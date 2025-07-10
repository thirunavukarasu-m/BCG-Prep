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


# Recursive Pre Order Traversal (DFS) Time: O(N) Space: O(N)

def pre_order(node):
    # This is the base case. When the right or left is None we just return.
    if not node:
        return
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)
    
# pre_order(a)

def in_order(node):
    # This is the base case. When the right or left is None we just return.
    if not node:
        return

    in_order(node.left)
    print(node)
    in_order(node.right)
    
# in_order(a)

def post_order(node):
    # This is the base case. When the right or left is None we just return.
    if not node:
        return

    post_order(node.left)
    post_order(node.right)
    print(node)
    
# post_order(a)



def pre_order_iterative(node):
    stack = [node]
    while stack:
        node = stack.pop()
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        print(node)
        
# pre_order_iterative(a)


# The above functions are DFS:
# 
# BFS

from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        print(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
bfs(a)