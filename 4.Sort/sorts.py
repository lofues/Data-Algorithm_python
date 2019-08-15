'''
	冒泡排序，插入排序，选择排序
	
'''

def bubble_sort(l : list):
	length = len(l)
	if length <= 1: return
	for i in range(length):
		flag = False
		for j in range(length-i-1):
			if l[j] > l[j+1]:
				l[j], l[j+1] = l[j+1], l[j]
				flag = True
		if not flag: break

def insert_sort(l : list):
	length = len(l)
	if length <= 1: return
	for i in range(1,length):
		value = l[i]
		j = i-1
		while j >= 0 and l[j] > value:
			l[j+1] = l[j]
			j -= 1
		l[j+1] = value


def selection_sort(l : list):
	length = len(l)
	if length <= 1: return
	for i in range(length):
		min_v,min_index = l[i],i
		for j in range(i,length):
			if l[j] < min_v:
				min_v,min_index = l[j], j
		l[i],l[min_index] = l[min_index],l[i]


def main():
	unsort = [x for x in range(6,0,-1)]
	#insert_sort(unsort)
	#bubble_sort(unsort)
	selection_sort(unsort)
	print(unsort)

if __name__ == '__main__':
	main()