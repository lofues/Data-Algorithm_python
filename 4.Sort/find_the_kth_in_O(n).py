'''
	在O(n)时间内找到第k大元素

	Author by : Lofues
'''

from typing import List

def find_the_kth(l : List[int], k : int) -> int:
	low, high = 0, len(l) - 1
	if k <= high + 1:
			key = partion(l,0,high)
			while key + 1 != k:
				if key + 1 < k :
					key = partion(l,key+1,high)
				else:
					key = partion(l,0,key-1)
			return l[key]

def partion(l : List[int], low : int, high : int):
	pivot = l[high]
	i = j = low
	for j in range(low,high):
		if l[j] < pivot:
			l[i], l[j] = l[j], l[i]
			i += 1
	l[i],l[high] = l[high],l[i]
	return i


l = [2,3,7,1,-4,5,11,34,2,54,343,3]
print(l)

print(find_the_kth(l,3))
print(l)