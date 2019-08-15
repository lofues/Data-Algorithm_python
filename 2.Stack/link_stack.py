'''
	用无头节点的单链表实现栈

	Author by: Junfu Wang
'''
class Node(object):
	def __init__(self,val):
		self.val = val
		self.next = None

class LinkedStack(object):
	def __init__(self):
		self.n = 0
		self.top = None

	def push(self,val : int):
		# 栈的插入操作：头插法
		new_node = Node(val)
		new_node.next = self.top
		self.top = new_node
		self.n += 1

	def pop(self) -> int:
		if self.empty():
			return None
		else:
			x = self.top.val
			self.n -= 1
			self.top = self.top.next
			return x

	def __len__(self) -> int:
		return self.n

	def empty(self) -> bool:
		return self.n == 0

	def __repr__(self):
		cur = self.top
		result = []
		while cur:
			result.append(cur.val)
			cur = cur.next
		return '->'.join(str(x) for x in result)

def main1():
	ls = LinkedStack()
	for i in range(10):
		ls.push(i)
	print(ls,len(ls))
	print(ls.pop())
	print(ls)
	print(len(ls))


if __name__ == '__main__':
	main()