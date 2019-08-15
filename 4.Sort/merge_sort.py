'''
	对数组实现归并排序
	
	Author by: Lofues
'''

from typing import List


def merge_sort(l : List[int]):
	Merge_Sort(l, 0, len(l) - 1)

def Merge_Sort(l : List[int], low : int, high : int):
	if low < high:
		mid = low + (high - low) // 2
		Merge_Sort(l,low,mid)
		Merge_Sort(l,mid+1,high)
		merge(l,low,mid,high)

def merge(l: List[int], low : int, mid : int, high : int):
	tmp = []
	i, j = low, mid + 1
	while i <= mid and j <= high:
		if l[i] <= l[j]:
			tmp.append(l[i])
			i+=1
		else:
			tmp.append(l[j])
			j+=1
	tmp.extend(l[i:mid+1]) if i <= mid else tmp.extend(l[j:high + 1])
	l[low:high+1] = tmp

