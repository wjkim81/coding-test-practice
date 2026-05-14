from __future__ import annotations

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: TreeNode | None) -> bool:
    if root is None:
        return True
    

    def max_depth(root: TreeNode | None) -> int:
        if root is None:
            return 0
        
        left_depth = max_depth(root.left)
        right_depth = max_depth(root.right)

        if left_depth == -1 or right_depth == -1:
            return -1
        if abs(left_depth - right_depth) > 1:
            return -1
        
        return max(left_depth, right_depth) + 1
    
    return max_depth(root) != -1
