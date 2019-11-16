'''
	解决二分查找的第一种变形问题: 
	1.找到第一个相同元素下标
	2.找到最后一个相同元素的下标
	3.找到第一个大于等于该元素的下标
	4.找到最后一个小于等于该元素的下标

	Author by: Lofues
'''

def binary_search(a : list, n : int, val : int) -> int:
	return Binary_search_find_the_first(a,0,n-1,val)
	#return Binary_search_find_the_last(a,0,n-1,val)
	#return Binary_search_find_the_first_ge(a,0,n-1,val)
	#return Binary_search_find_the_last_let(a,0,n-1,val)



def Binary_search_find_the_first(a : list, start : int, end : int, val : int) -> int:
	if start > end: return -1
	low,high = start,end
	while low <= high:
		mid = low + (high - low) // 2
		if val < a[mid]:
			high = mid - 1
		elif val > a[mid]:
			low = mid + 1
		else:
			# 如果相等元素是数组第一个元素或者前边一个元素不为val则返回
			if mid == start or a[mid-1] != val: return mid
			high = mid - 1
	return -1


def Binary_search_find_the_last(a: list, start : int, end : int, val : int) -> int:
	if start > end: return -1
	low,high = start,end
	while low <= high:
		mid = low + (high - low) // 2
		if val < a[mid]:
			high = mid - 1
		elif val > a[mid]:
			low = mid + 1
		else:
			# 如果相等元素是数组最后一个元素或者后边的一个元素不为val则返回
			if mid == end - 1 or a[mid+1] != val: return mid
			low = mid + 1
	return -1

def Binary_search_find_the_first_ge(a : list, start : int, end : int, val : int) -> int:
	# 找到第一个大于等于该元素的index
	if start > end: return -1
	low,high = start,end
	while low <= high:
		mid = low + (high - low) // 2
		if a[mid] >= val:
			if mid == start or a[mid - 1] < val:
				return mid
			else:
				high = mid - 1
		else:
			low = mid + 1
	return -1

def Binary_search_find_the_last_le(a : list, start : int, end : int, val :int) -> int:
	if start > end: return -1
	low,high = start,end
	while low <= high:
		mid = low + (high - low) // 2
		if a[mid] <= val:
			if mid == end - 1 or a[mid + 1] > val:
				return mid
			else:
				low = mid + 1
		else:
			high = mid - 1
	return -1
			

def main():
	a = [1,1,1,1,2,3,4,5,6,6,6,6,7,7,9,10]
	print(binary_search(a,len(a),8))
	print(a[13])

if __name__ == '__main__':
	main()
