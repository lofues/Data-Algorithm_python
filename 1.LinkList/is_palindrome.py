# 创建一个多链表并判断是否是回文

class Linklist(object):
	def __init__(self,val = 1):
		self.val = val
		self.next = None

def insert_node(l : Linklist,val : int) -> Linklist:
	# 向链表中插入节点
	top = l
	while top.next != None:
		top = top.next
	top.next = Linklist(val)
	return l

def is_palindrome(l : Linklist) -> bool:
	s = ''
	if l.next == None:
		return False
	elif l.next.next == None:
		return str(l.next.val)
	cur = l.next
	while cur != None:
		s += str(cur.val)
		cur = cur.next 
	return s == s[::-1]

def main():
	dummyhead = Linklist()
	for i in range(10):
		insert_node(dummyhead,i)
	for i in range(9,-1,-1):
		insert_node(dummyhead,i)
	print(is_palindrome(dummyhead))


if __name__ == '__main__':
	main()