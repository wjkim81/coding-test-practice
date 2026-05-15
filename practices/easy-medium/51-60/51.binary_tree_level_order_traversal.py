from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root: TreeNode | None) -> List[List[int]]:
    if root is None:
        return []
    
    q = deque()
    q.append(root)

    result = []

    while q:
        level_node = []
        for _ in range(len(q)):
            node = q.popleft()
            level_node.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level_node)

    return result