'''
	实现计数排序

	Author by: Lofues
'''

def counting_sort(a : list):
	# 数据范围必须为非负整数且大于0
	max_item = a[0]
	for i in range(len(a)):
		if a[i] > max_item:
			max_item = a[i]
	b = [0] * (max_item + 1)
	for i in range(len(a)):
		# b中存储每个值的个数
		b[a[i]] += 1
	for i in range(1,len(b)):
		# b中每个位置存储小于该值的元素个数
		b[i] += b[i-1]
	c = [0] * len(a)
	for i in range(len(a)-1,-1,-1):
		index = b[a[i]] - 1
		b[a[i]] -= 1
		c[index] = a[i]
	a[0:len(a)-1] = c[0:len(c)-1]

a = [6,4,6,3,2,5,7,4,2,5,7,4,2,2,5,3,5,2,35,34,21,12]
counting_sort(a)
print(a)