'''
	实现数组快排

	Author by: Lofues
'''

from typing import List
import random

def quick_sort(a : List[int]):
	Quick_Sort(a, 0, len(a) - 1)

def Quick_Sort(a : List[int], low : int, high: int):
	if low < high:
		# 随机选择pivot的位置
		k = random.randint(low,high)
		a[k], a[high] = a[k], a[high]
		
		pivot = partion(a,low,high)
		Quick_Sort(a,low,pivot-1)
		Quick_Sort(a,pivot+1,high)

def partion(a : List[int], low : int, high : int) -> int:
	pivot = a[high]
	i = j = low
	# 让j从头遍历到high之前的一个位置
	for j in range(low,high):
		if a[i] < pivot:
			a[i], a[j] = a[j], a[i]
			i += 1
	# 交换pivot与a[i]
	a[high], a[i] = a[i], a[high]
	return i

a = [x for x in range(8,0,-1)]
quick_sort(a)
print(a)