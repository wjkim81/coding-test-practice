from __future__ import annotations

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(node: TreeNode | None) -> TreeNode | None:
    if node is None:
        return None

    node.left, node.right = node.right, node.left

    invert_tree(node.left)
    invert_tree(node.right)

    return node