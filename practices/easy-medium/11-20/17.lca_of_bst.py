from __future__ import annotations

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca_of_bst(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    if root is None:
        return None
    
    if p.val < root.val and q.val < root.val:
        return lca_of_bst(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lca_of_bst(root.right, p, q)
    
    else:
        return root
    
