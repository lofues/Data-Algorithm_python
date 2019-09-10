"""
    用小顶堆动态维护数组的前k大元素
    Author By: Lofues
"""
from heap import MinHeap
import random

def get_top_k(nums,k):
    """
    返回数组的前k大元素
    :param nums:
    :param k:
    :return:
    """
    if len(nums) < k:
        return nums

    min_heap = MinHeap(nums[:k],k)

    for i in range(k,len(nums)):
        heap_top = min_heap.get_top()
        if nums[i] > heap_top:
            min_heap.remove_top()
            min_heap.insert(nums[i])

    return min_heap.get_data()


if __name__ == "__main__":
    nums = []
    k = 3

    for i in range(20):
        nums.append(random.randint(1,100))

    print("--- nums ---")
    print(nums)

    print('--- top 3 ---')
    print(get_top_k(nums,k))
















