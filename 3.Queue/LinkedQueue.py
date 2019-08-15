'''
	用链表实现队列

	Author by: Lofues
'''

from typing import Optional

class Node(object):
	def __init__(self,val = None):
		self.val = val
		self.next = None

class LinkedQueue(object):
	def __init__(self):
		self._tail = None
		self._head = None

	def enqueue(self,val : Optional[str]):
		new_node = Node(val)
		if self._tail:
			self._tail.next = new_node
		else:
			self._head = new_node
		self._tail = new_node

	def dequeue(self) -> Optional[str]:
		if self._head:
			ans = self._head.val
			self._head = self._head.next
			if not self._head:
				self._tail = None
			return ans

	def __repr__(self) -> str:
		cur = self._head
		result = []
		while cur:
			result.append(cur.val)
			cur = cur.next
		return '->'.join(str(x) for x in result)


def main():
	lq = LinkedQueue()
	for i in range(10):
		lq.enqueue(i)
	print(lq)
	for i in range(5):
		lq.dequeue()
	print(lq)
	for i in range(5):
		lq.enqueue(i)
	print(lq)


if __name__ == '__main__':
	main()