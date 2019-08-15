'''
	 用数组创建队列并支持动态移位操作

	 Author by: Lofues
'''

from typing import Optional

class ArrayQueue(object):
	def __init__(self,capacity : int):
		self._capacity = capacity
		self._items = []
		self._head, self._tail = 0, 0

	def enqueue(self,item : str) -> bool:
		# 判断是否已满
		if self._tail == self._capacity:
			if self._head == 0:
				return False
			else:
				self._items[0:self._tail-self._head] = self._items[self._head:self._tail]
				self._tail -= self._head
				self._head = 0
		self._items.insert(self._tail,item)
		self._tail += 1
		return True

	def dequeue(self) -> Optional[str]:
		# 从队头取出数据
		if self._head == self._tail:
			return None
		else:
			item = self._items[self._head]
			self._head += 1
			return item

	def __repr__(self):
		if self._head == self._tail:
			return None
		else:
			result = []
			cur = self._head
			while cur != self._tail:
				result.append(self._items[cur])
				cur += 1
		return '->'.join(str(x) for x in result)


def main():
	queue = ArrayQueue(10)
	for i in range(10):
		queue.enqueue(i)
	print(queue)
	for i in range(5):
		print(queue.dequeue())
	print(queue)

if __name__ == '__main__':
	main()