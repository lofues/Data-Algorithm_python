"""
    演示二叉树的前中后序遍历

    Author by: Lofues
"""

class treenode():
    def __init__(self, val : int):
        assert isinstance(val,int)

        self.val = val
        self.left = None
        self.right = None

def pre_order(node: treenode):
    if  node:
        res = []
        res.append(node.val)
        res.extend(pre_order(node.left))
        res.extend(pre_order(node.right))
        return res
    else:
        return []

def in_order(node : treenode) -> list:
    if node:
        res = []
        res.extend(in_order(node.left))
        res.append(node.val)
        res.extend(in_order(node.right))
        return res
    else:
        return []

def post_order(node : treenode) -> list:
    if  node:
        res = []
        res.extend(post_order(node.left))
        res.extend(post_order(node.right))
        res.append(node.val)
        return res
    else:
        return []


def main():
    root = treenode(2)
    root_left = treenode(1)
    root_right = treenode(3)

    root.left = root_left
    root.right = root_right

    print(pre_order(root))
    print(in_order(root))
    print(post_order(root))

if __name__ == '__main__':
    main()

