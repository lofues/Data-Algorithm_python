'''
	使用递归和非递归实现二分查找

	Author by: Lofues
'''

def binary_search(a : list, n : int, val : int) -> int:
	#return Binary_search(a,0,n-1,val)
	return binary_search_rec(a,0,n-1,val)

def Binary_search(a : list, low : int, high : int, val: int) -> int:
	while low <= high:
		mid = low + (high - low) // 2
		if a[mid] == val:
			return mid
		elif val < a[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return -1

def binary_search_rec(a : list, low : int, high : int, val : int) -> int:
	if low > high: return -1
	mid = low + (high - low) // 2
	if a[mid] == val:
		return mid
	elif val < a[mid]:
		high = mid - 1
		return binary_search_rec(a,low,high,val)
	else:
		low = mid + 1
		return binary_search_rec(a,low,high,val)


a = [x for x in range(0,50,2)]
print(binary_search(a,50,21))