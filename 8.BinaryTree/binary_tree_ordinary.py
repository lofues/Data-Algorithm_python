"""
    二叉树的常见算法实现：计算深度、计算节点个数、

    Author by：Lofues
"""
from functools import lru_cache
from queue import Queue

class Node():
    def __init__(self,val = None):
        self.val = val
        self.left = None
        self.right = None


@lru_cache(maxsize = None)
def cur_parse_num(root):
    """
    递归法计算二叉树的节点个数
    :param root:
    :return:
    """
    if root is None:
        return 0
    return cur_parse_num(root.left) + cur_parse_num(root.right) + 1

@lru_cache(maxsize=None)
def cur_parse_height(root):
    """
    递归法计算二叉树的高度
    :param root:
    :return:
    """
    if root is None:
        return 0
    return max(cur_parse_height(root.left),cur_parse_height(root.right))+1

def parse_height(root):
    """
    非递归法计算二叉树的高度
    :param root:
    :return:
    """
    if not isinstance(root,Node):
        return None
    ret = 0
    q = Queue()
    q.put((root,1))
    while not q.empty():
        cur_node,cur_layer = q.get()
        if cur_node:
            q.put((cur_node.left,cur_layer+1))
            q.put((cur_node.right,cur_layer+1))
            ret = cur_layer + 1
    return ret - 1

def cur_parse_leaf_num(root):
    """
    递归计算树的叶子节点个数
    :param root:
    :return:
    """
    if root is None:
        return 0
    if root and root.left is None and root.right is None:
        return 1
    return cur_parse_leaf_num(root.left) + cur_parse_leaf_num(root.right)

def parse_leaf_num(root):
    """
    非递归计算树的叶子节点个数
    :param root:
    :return:
    """
    if not isinstance(root,Node):
        return None
    q = Queue()
    q.put(root)
    ret = 0
    while not q.empty():
        node = q.get()
        if node:
            q.put(node.left)
            q.put(node.right)
            if node.left is None and node.right is None:
                ret += 1
    return ret

@lru_cache(maxsize = None)
def cur_parse_k_level_num(root,k):
    """
    递归计算第k层的节点个数
    :param root:
    :return:
    """
    if root and not isinstance(root,Node):
        return None
    if not root or k <= 0:
        return 0
    # 计算左子树与右子树上的叶子节点个数
    if root and k == 1:
        return 1

    return cur_parse_k_level_num(root.left,k-1) + cur_parse_k_level_num(root.right,k-1)

def parse_k_level_num(root,k):
    """
    非递归计算第k层叶子节点个数
    使用层次遍历
    :param root:
    :param k:
    :return:
    """
    if root and not isinstance(root,Node):
        return None
    if root is None:
        return None

    q = Queue()
    q.put((root,1))
    ret = 0
    while not q.empty():
        cur_node,cur_level = q.get()
        if cur_node:
            if cur_level > k:
                break
            q.put((cur_node.left,cur_level+1))
            q.put((cur_node.right,cur_level+1))
            if cur_level == k:
                ret += 1
    return ret

@lru_cache(maxsize=None)
def cur_is_same_tree(root1,root2):
    if not root1 and not root2:
        return True

    if root1 and root2:
        return (root1.val==root2.val) and cur_is_same_tree(root1.left,root2.left) and cur_is_same_tree(root1.right,root2.right)
    else:
        return False

def is_bst(root):
    """
    判断此树是否是二分查找树
    使用中序遍历是否递增
    :param root:
    :return:
    """
    if root and not isinstance(root, Node):
        return None
    def is_asc(items):
        for i in range(len(items)-1):
            if items[i] > items[i+1]:
                return False
        return True
    @lru_cache(maxsize=None)
    def in_order(root):
        if not root:
            return []

        ret = []
        ret.extend(in_order(root.left))
        ret.append(root.val)
        ret.extend(in_order(root.right))
        return ret
    if is_asc(in_order(root)):
        return True
    else:
        return False


# 定义树1：root 和树2：root1
root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.left.left = Node(0)

root1 = Node(2)
root1.left = Node(1)
root1.right = Node(3)
root1.left.left = Node(0)
root1.right.left = Node(4)

# 递归计算二叉树节点个数
print(cur_parse_num(root))

# 递归计算二叉树高度
print(cur_parse_height(root))
print(parse_height(root))

# 计算叶子节点的个数
print(cur_parse_leaf_num(root))
print(parse_leaf_num(root))

# 计算第k层的叶子节点个数
print('第1层:',cur_parse_k_level_num(root,1))
print('第2层:',cur_parse_k_level_num(root,2))
print('第3层:',cur_parse_k_level_num(root,3))

print('第1层:',parse_k_level_num(root,1))
print('第2层:',parse_k_level_num(root,2))
print('第3层:',parse_k_level_num(root,3))
# 判断两个树是否相同
print(cur_is_same_tree(root,root1))

# 判断此树是否是二分查找树
print('root is bst?',is_bst(root))
print('root1 is bst?',is_bst(root1))


