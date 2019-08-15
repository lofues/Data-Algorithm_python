'''
	实现hashtable

	采用链接表法解决冲突问题

	Author by: Lofues
'''

class LinearTable(object):
	def __init__(self):
		self.items = []

	def add(self,k,v):
		self.items.append((k,v))

	def get(self,k):
		for key,val in self.items:
			if key == k:
				return val
		raise KeyError


class BetterTable(object):
	def __init__(self,n):
		self.maps = []
		self.capacity = n
		for i in range(n):
			self.maps.append(LinearTable())

	def find_table(self,k):
		index = hash(k) % self.capacity
		return self.maps[index]

	def add(self,k,v):
		m = self.find_table(k)
		m.add(k,v)

	def get(self,k):
		m = self.find_table(k)
		return m.get(k)

class HashTable(object):
	def __init__(self):
		self.maps = BetterTable(2)
		self.count = 0

	def get(self,k):
		return self.maps.get(k)

	def add(self,k,v):
		if self.count == len(self.maps.maps):
			self.resize()

		self.maps.add(k,v)
		self.count += 1

	def resize(self):
		new_table = BetterTable(self.count * 2)

		for m in self.maps.maps:
			for k,v in m.items:
				new_table.add(k,v)

		self.maps = new_table

def test():
	Table = HashTable()
	test = [
		('banana',11),
		('apple',2),
		('key',22),
		('panda',0)
	]
	for key,val in test:
		Table.add(key,val)
	print(Table.get('banana'))
	print(Table.get('key'))
	print(Table.get('xiha'))

test()