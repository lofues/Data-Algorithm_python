
"""
    判断一个树是否是平衡二叉查找树
"""
from functools import lru_cache

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isBalanced(root) -> bool:
    if root and not isinstance(root, TreeNode):
        return False
    if root is None:
        return True
    return abs(parse_height(root.left) - parse_height(root.right)) <= 1

@lru_cache(maxsize=None)
def parse_height(root):
    if root is None:
        return 0
    if root and root.left is None and root.right is None:
        return 1
    return max(parse_height(root.left), parse_height(root.right)) + 1

root = TreeNode(2)
root.left = TreeNode(1)
root.left.left = TreeNode(1)
print(parse_height(root))