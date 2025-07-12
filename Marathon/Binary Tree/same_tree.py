'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true


Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104

https://leetcode.com/problems/same-tree/description/
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# This solution has a logic issue.
# Different trees can have same inorder traversal.
class Solution:
    def in_order_traversal(self, root, arr):
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            print(current.val == None)
            arr.append(current.val)

            current = current.right

        return arr

    def isSameTree(self, p, q):
        in_order_p = self.in_order_traversal(p,[])
        in_order_q = self.in_order_traversal(q,[])

        return in_order_p == in_order_q
        
# This will work
# first if - checks the base condition till the leaf nodes and beyond.
# We don't have a return True apart from that cause if it doesn't match it'll fail and return False before the base condition. If it reaches the base condition then it is all good.
class Solution_1:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)