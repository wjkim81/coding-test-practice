class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree(root: TreeNode | None) -> int:
    max_diameter = 0

    def max_depth(node: TreeNode | None) -> int:
        nonlocal max_diameter

        if node is None:
            return 0

        left_depth = max_depth(node.left)
        right_depth = max_depth(node.right)

        max_diameter = max(max_diameter, left_depth + right_depth)

        return max(left_depth, right_depth) + 1

    max_depth(root)
    return max_diameter
