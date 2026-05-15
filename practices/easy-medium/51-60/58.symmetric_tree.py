class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root: TreeNode | None) -> bool:
    if root is None:
        return True
    
    def mirror(a: TreeNode, b: TreeNode) -> bool:
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        return mirror(a.left, b.right) and mirror(a.right, b.left)
    
    return mirror(root.left, root.right)