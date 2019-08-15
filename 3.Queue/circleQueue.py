'''
	用数组创建循环队列

	Author by: Lofues
'''

class CircularQueue(object):
	def __init__(self,capacity : int):
		self._head, self._tail = 0,0
		self._capacity = capacity + 1
		self._items = [None] *  self._capacity

	def is_full(self):
		return (self._tail + 1) % self._capacity == self._head

	def is_empty(self):
		return self._tail == self._head

	def dequeue(self) -> bool:
		if self.is_empty():
			return False
		else:
			self._items[self._head] = None
			self._head = (self._head + 1) % self._capacity
			return True

	def enqueue(self,val) -> bool:
		if self.is_full():
			return False
		else:
			self._items[self._tail] = val
			self._tail = (self._tail + 1) % self._capacity
			return True

	def __repr__(self):
		if self.is_empty():
			return None
		else:
			result = []
			cur = self._head
			while cur != self._tail:
				result.append(self._items[cur])
				cur = (cur + 1) % self._capacity
			return '->'.join(str(x) for x in result)

	def prior(self):
		return self._items[self._head] if not self.is_empty() else -1

	def tail(self):
		return self._items[(self._tail - 1 + self._capacity) % self._capacity] if not self.is_empty() else -1

def main():
	queue = CircularQueue(10)
	for i in range(10):
		queue.enqueue(i)
	print(queue)
	for i in range(5):
		queue.dequeue()
	print(queue)
	print(queue.prior(),queue.tail())
	for i in range(5):
		queue.enqueue(i)
	print(queue)

if __name__ == '__main__':
	main()