from collections import deque
def levelOrder(root):
    if not root:
        return []
    result = []
    queue = deque()
    queue.append(root)
    
    while queue:
        level_length = len(queue)
        level_nodes = []

        for _ in range(level_length):
            popped = queue.popleft()
            level_nodes.append(popped.val)

            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
        
        result.append(level_nodes)
    return result