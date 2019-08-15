'''
	用二分查找方法查找一个数的平方根，误差不小于e-7

	Author by : Lofues
'''
def get_sqrt(n : int) -> float:
	if n < 0: return None
	precison = 1e-7
	low, high = 0, n
	while high - low >= precison:
		mid = low + (high - low) / 2
		if mid * mid < n:
			low = mid
		elif mid * mid > n:
			high = mid
		else: 
			return mid 
	return high 
print(get_sqrt(2))