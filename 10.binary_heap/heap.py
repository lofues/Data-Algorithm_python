"""
    实现大顶堆和小顶堆
    Author by: Lofues
"""

import math
import random

class Heap:
    def __init__(self,nums = None,capacity = 100):
        self._data = []
        self._capacity = capacity
        if type(nums) == list and len(nums) <= capacity:
            for num in nums:
                assert type(num) is int
                self._data.append(num)
        else:
            return
        self._length = len(self._data)
        self._heapify()

    def _heapify(self):
        if self._length <= 1:
            return

        # idx of the last parent
        idx = self._length // 2 - 1

        for i in range(idx,-1,-1):
            self._heap_down(i)

    def _heap_down(self):
        pass

    def insert(self,num):
        pass

    def get_top(self):
        if self._length <= 0:
            return
        return self._data[0]

    def remove_top(self):
        if self._length <= 0:
            return

        self._data[0], self._data[-1] = self._data[-1], self._data[0]
        ret = self._data.pop()
        self._length -= 1
        self._heap_down(0)

        return ret

    def get_length(self):
        return self._length

    def get_data(self):
        return self._data

    @staticmethod
    def _draw_heap(data):
        """
        格式化打印
        :param data:
        :return:
        """
        length = len(data)

        if length == 0:
            return "empty heap"

        ret = ''
        for i,v in enumerate(data):
            ret += str(v)
            # 每行最后一个换行
            if i == 2 ** int(math.log(i + 1,2) + 1) - 2 or i == len(data) - 1:
                ret += "\n"
            else:
                ret += ', '

        return ret

    def __repr__(self):
        return self._draw_heap(self._data)


class MaxHeap(Heap):
    def _heap_down(self, idx):
        if self._length <= 1:
            return

        lp = self._length // 2 - 1

        # 依次向下堆化
        while idx <= lp:
            lc = idx * 2 + 1
            rc = idx * 2 + 2

            if rc <= self._length - 1:
                tmp = lc if self._data[lc] > self._data[rc] else rc
            else:
                tmp = lc

            if self._data[tmp] > self._data[idx]:
                self._data[tmp], self._data[idx] = self._data[idx], self._data[tmp]
                idx = tmp
            else:
                break

    def insert(self,num):
        if self._length >= self._capacity:
            return False

        self._data.append(num)
        self._length += 1

        # 插入节点的位置索引向上堆化
        idx = self._length - 1

        while idx > 0:
            p = (idx - 1) // 2

            if self._data[idx] > self._data[p]:
                self._data[idx], self._data[p] = self._data[p], self._data[idx]
                idx = p
            else:
                break

        return True

class MinHeap(Heap):
    def _heap_down(self,idx):
        if self._length <= 1:
            return

        # 找到最后一个父节点
        lp = self._length // 2 - 1

        while idx <= lp:
            lc = idx * 2 + 1
            rc = idx * 2 + 2

            # 找到子节点中的最小节点
            if rc <= self._length - 1:
                tmp = lc if self._data[lc] < self._data[rc] else rc
            else:
                tmp = lc

            # 让最小节点父节点交换
            if self._data[tmp] < self._data[idx]:
                self._data[tmp], self._data[idx] = self._data[idx], self._data[tmp]
                idx = tmp
            else:
                break

    def insert(self,num):
        if self._length >= self._capacity:
            return False

        self._data.append(num)
        self._length += 1

        # 找出最后一个节点的下标并向上堆化
        idx = self._length - 1

        while idx > 0:
            p = (idx - 1) // 2

            if self._data[p] > self._data[idx]:
                self._data[idx], self._data[p] = self._data[p], self._data[idx]
                idx = p
            else:
                break

        return True



def main():
    min_heap = MinHeap([2,5,3,1,6,4,23,34],100)
    max_heap = MaxHeap([2,5,3,1,6,4,23,34],100)

    print(min_heap)
    print(max_heap)

    min_heap.insert(32)
    max_heap.insert(32)

    print(min_heap)
    print(max_heap)


if __name__ == "__main__":
    main()






