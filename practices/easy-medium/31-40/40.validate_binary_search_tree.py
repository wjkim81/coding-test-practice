class NodeTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def validate_bst(root: NodeTree | None) -> bool:
    def dfs(node: NodeTree | None, min_val: float, max_val: float) -> bool:
        if node is None:
            return True

        if not (min_val < node.val < max_val):
            return False

        return (
            dfs(node.left, min_val, node.val)
            and dfs(node.right, node.val, max_val)
        )

    return dfs(root, float("-inf"), float("inf"))
