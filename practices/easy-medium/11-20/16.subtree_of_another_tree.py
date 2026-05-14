from __future__ import annotations

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def same_tree(node1: TreeNode | None, node2: TreeNode | None) -> bool:
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    if node1.val != node2.val:
        return False

    return same_tree(node1.left, node2.left) and same_tree(node1.right, node2.right)

def subtree_of_another_tree(root: TreeNode | None, sub_root: TreeNode | None) -> bool:
    if sub_root is None:
        return True
    if root is None:
        return False

    if same_tree(root, sub_root):
        return True

    return subtree_of_another_tree(root.left, sub_root) or subtree_of_another_tree(root.right, sub_root)