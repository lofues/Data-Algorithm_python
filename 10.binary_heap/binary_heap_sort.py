"""
    实现顶排序
    Author By: Lofues
"""

from binary_heap import BinaryHeap

class BinaryHeapSort(BinaryHeap):
    def __init__(self):
        super(BinaryHeapSort,self).__init__()

    def sort(self,nums):
        assert type(nums) is list

        if len(nums) <= 1:
            return

        self._type_assert(nums)

        # 对原始数组进行堆化
        self._heapify(nums,len(nums)-1)

        # sort
        idx = len(nums) - 1
        for i in range(idx,0,-1):
            nums[0], nums[i] = nums[i], nums[0]
            self._heap_down(nums,0,i-1)

        return



def main():
    bhs = BinaryHeapSort()
    nums = [3, 5, 2, 6, 1, 7, 6]

    print("--- before sort ----")
    print(nums)

    print("--- after sort ---")
    bhs.sort(nums)
    print(nums)

main()








