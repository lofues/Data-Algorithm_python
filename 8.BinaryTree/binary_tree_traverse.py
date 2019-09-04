"""
    二叉树前中后序遍历的递归与非递归的实现以及层次遍历

    Author by：Lofues
"""
import time
import functools
from queue import Queue

def parse_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        ret = func(*args,**kwargs)
        end = time.time()
        return ret
    return wrapper



class Node(object):
    def __init__(self,val = None):
        self.left = None
        self.right = None
        self.val = val

def cur_preorder(node):
    if node is None: return []

    ret = []
    ret.append(node.val)
    ret.extend(cur_preorder(node.left))
    ret.extend(cur_preorder(node.right))
    return ret

def cur_inorder(node):
    if node is None: return []

    ret = []
    ret.extend(cur_inorder(node.left))
    ret.append(node.val)
    ret.extend(cur_inorder(node.right))
    return ret

def cur_postorder(node):
    if node is None: return []

    ret = []
    ret.extend(cur_postorder(node.left))
    ret.extend(cur_postorder(node.right))
    ret.append(node.val)
    return ret



def pre_order(root):
    if not isinstance(root,Node):
        return None
    ret = []
    stack = [root]
    while stack:
        node = stack.pop(-1)
        if node:
            ret.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return ret

def in_order(root):
    """
    将处理过程分治为三个方面：左子树、根节点值、右子树
    :param root:
    :return:
    """
    if not isinstance(root,Node):
        return None
    ret = []
    stack = [root.right,root.val,root.left]
    while stack:
        tmp = stack.pop(-1)
        if tmp:
            if isinstance(tmp,Node):
                stack.append(tmp.right)
                stack.append(tmp.val)
                stack.append(tmp.left)
            else:
                ret.append(tmp)
    return ret

def post_order(root):
    """
    将处理过程分治为三个方面：左子树、右子树、根节点值
    :param root:
    :return:
    """
    if not isinstance(root,Node):
        return None
    ret = []
    stack = [root.val,root.right,root.left]
    while stack:
        tmp = stack.pop(-1)
        if tmp:
            if isinstance(tmp,Node):
                stack.append(tmp.val)
                stack.append(tmp.right)
                stack.append(tmp.left)
            else:
                ret.append(tmp)
    return ret

def level_order(root):
    """
    层次遍历二叉树
    :param root:
    :return:
    """
    if not isinstance(root,Node):
        return None

    ret = []
    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        if node:
            ret.append(node.val)
            q.put(node.left)
            q.put(node.right)
    return ret


root = Node(2)
root.left = Node(1)
root.right = Node(3)

# 前中后序遍历
print(cur_preorder(root))
print(pre_order(root))
print(cur_inorder(root))
print(in_order(root))
print(cur_postorder(root))
print(post_order(root))

# 层次遍历
print(level_order(root))




















