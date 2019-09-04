"""
    演示二叉查找树的基本用法

    Author by : Lofues
"""

class TreeNode():
    def __init__(self, val : int):
        assert isinstance(val,int)

        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self,l : list):
        self.root = None

        for _ in l:
            self.insert(_)

    def delete_test(self, val : int):
        assert isinstance(val,int)

        if not self.root:
            return
        parent = None

















    def delete(self, val : int):
        assert isinstance(val,int)
        if not self.root:
            return

        node = self.root
        parent = None
        while node and node.val != val:
            parent = node
            node = node.left if val < node.val else node.right

        # 如果不存在则返回
        if not node: return

        # 如果删除节点有两个子节点
        if node.left and node.right:
            successor_parent = node
            successor = node.right
            while successor.left:
                successor_parent = tmp
                successor = successor.left

            # 将两节点情况转换为单子节点或叶子节点
            node.val = successor.val
            parent,node = successor_parent,successor

        # 删除单子节点或者叶子节点
        child = node.left if node.left else node.right
        # 如果该树只有根节点
        if not parent:
            self.root = None
        else:
            if node.val < parent.val:
                parent.left = child
            else:
                parent.right = child



    def find(self,val : int) -> bool:
        if not self.root:
            return False
        node = self.root
        while node and node.val != val:
            node = node.left if val < node.val else node.right
        if node:
            return True
        else:
            return False

    def insert(self,val : int):
        assert isinstance(val,int)

        parent = None
        node = self.root
        while node:
            parent = node
            node = node.left if val < node.val else node.right

        # 如果为空树
        if not parent:
            self.root = TreeNode(val)
        else:
            if val < parent.val:
                parent.left = TreeNode(val)
            else:
                parent.right = TreeNode(val)

    def find_min(self):
        """
        找到树的最小值
        :return: int
        """
        if not self.root:
            return None
        else:
            node = self.root
            while node.left:
                node = node.left
            return node.val

    def find_max(self):
        """
        找到树的最大值
        :return: int
        """
        if not self.root:
            return None
        else:
            node = self.root
            while node.right:
                node = node.right
            return node.val

    def in_order(self):
        return self._in_order(self.root)

    def _in_order(self, node : TreeNode) -> list:
        if not node:
            return []
        else:
            ret = []
            ret.extend(self._in_order(node.left))
            ret.append(node.val)
            ret.extend(self._in_order(node.right))
            return ret

    def __repr__(self):
        return str(self.in_order())

    def get_root(self) -> int:
        if self.root:
           return self.root.val

def main():
    root = BinarySearchTree([5,5,2,1,3,6,7,8])
    print(root)
    print(root.find(8))
    print(root.find(0))
    root.delete(5)
    print(root)
    print('root is ',root.get_root())
    root.delete(8)
    print(root)
    root.delete(2)
    print(root)
    root.delete(6)
    print(root)
    root.delete(1)
    print(root)
    root.delete(3)
    print(root)
    root.delete(7)
    print(root)
    root.delete(5)
    print(root)
    print(root.get_root())
    root.delete(5)
    print(root)


if __name__ == '__main__':
    main()