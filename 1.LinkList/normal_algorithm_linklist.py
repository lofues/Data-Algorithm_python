'''
	完成以下常见链表代码
	1.单链表反转
 	2.链表中环的检测
	3.两个有序链表的合并
	4.删除链表倒数第n个节点
	5.求链表的中间节点
'''

class Linklist(object):
	def __init__(self,val = -1):
		self.val = val
		self.next = None


def reversed_link(l : Linklist) -> Linklist:
	'''
		翻转单链表
	'''
	if l.next == None or l.next.next == None:
		return l.next
	reversed_head = Linklist()
	while l.next != None:
		# 从前向后从原链表中取出节点用头插法插入新链表中
		temp = l.next
		l.next = l.next.next
		temp.next = reversed_head.next
		reversed_head.next = temp
	return reversed_head

def check_loop(l : Linklist) -> bool:
	'''
		判断一个链表是否有环
	'''
	slow = fast = l
	# 循环判断快慢指针是否相等
	while fast and fast.next:
		# 如果fast指针能够指向空值说明必没有循环
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			return True
	return False

def find_middle_node(l : Linklist) -> Linklist:
	'''
		找到链表的中间节点并返回,若节点数为偶数则返回中间之后的节点
	'''
	slow, fast = l.next, l.next
	fast  = fast.next if fast else None
	while fast and fast.next:
		slow, fast = slow.next, fast.next.next
	return slow


def print_list(l : Linklist):
	'''
		打印链表
	'''
	if l.next == None:
		return None
	elif l.next.next == None:
		print(l.next.val)
	result = []
	cur = l.next
	while cur != None:
		result.append(cur.val)
		cur = cur.next
	print('->'.join([str(x) for x in result]))

def merge_sortedList(l1: Linklist,l2: Linklist) -> Linklist:
	'''
		合并两个有序单链表
	'''
	if  l1.next and l2.next:
		l3 = Linklist()
		cur = l3
		l1, l2 = l1.next, l2.next
		while l1 and l2:
			if l1.val <= l2.val:
				cur.next = l1
				l1 = l1.next
			else:
				cur.next = l2
				l2 = l2.next
			cur = cur.next
		cur.next = l1 if l1 else l2
		return l3
	else:
		return l1 or l2 # 返回l1或者l2之中非空的值

def remove_nth_from_end(l: Linklist,n : int) -> Linklist:
	'''
		带头结点
		假设n是大于0的整数
		删除链表的倒数第n个节点
	'''
	dummyhead = l
	fast,slow = l,l
	count = -1
	while fast and count < n:
		fast = fast.next
		count += 1
	if not fast and count < n:
		print('not so much nodes')
		return dummyhead
	if not fast and count == 0:
		dummyhead.next = dummyhead.next.next
		return dummyhead
	while fast:
		slow,fast = slow.next,fast.next
	slow.next = slow.next.next
	return dummyhead




def main():
	l1,l2 = Linklist(),Linklist()
	cur = l1
	for i in range(0,10,2):
		cur.next = Linklist(i)
		cur = cur.next
	cur = l2
	for i in range(1,9,2):
		cur.next = Linklist(i)
		cur = cur.next
	print_list(l1)
	print_list(l2)
	l3 = merge_sortedList(l1,l2)
	print_list(l3)
	print(remove_nth_from_end)

if __name__ == '__main__':
	main()



	
