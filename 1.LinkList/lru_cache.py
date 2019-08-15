#使用单链表实现lru_cache机制
#分为两种情况
#1.如果此数据之前已经被缓存到链表中了，遍历得到此节点并删除，然后插入到链表的头部。
#2.如果此数据之前没有被缓存到链表中，分为两种情况：
#	当缓冲没有满时，直接将其插入到头部
#	当缓存满时，将链表尾部节点删除并插入到头部
class LinkList(object):
	def __init__(self,val = None):
		self.val = val
		self.next = None

class LRUCache(object):
	def __init__(self,capicity):
		self.cap = capicity
		self.top = LinkList()
		self.hsmap = {}

	def get(self, val : int):
		if val in self.hsmap.keys():
			cur_pre = self.top
			while cur_pre.next != self.hsmap[val]:
				cur_pre = cur_pre.next
			# 删除节点并将其插入到链表头部
			cur = cur_pre.next
			cur_pre.next = cur.next
			cur.next = self.top.next
			self.top.next = cur

		else:
			# 增加新节点到首部
			cur = LinkList(val)
			cur.next = self.top.next
			self.top.next = cur
			self.hsmap[val] = cur

			if len(self.hsmap.keys()) > self.cap:
				# 删除尾节点
				del_node_pre = self.top
				while del_node_pre.next.next != None:
					del_node_pre = del_node_pre.next
				self.hsmap.pop(del_node_pre.next.val)
				del_node_pre.next = None


	def __repr__(self):
		result = ''

		cur = self.top.next
		while cur != None:
			result += (str(cur.val) + '->')
			cur = cur.next
		if not result:
			return result
		else:
			return result[:-2]

	def __len__(self) -> int:
		return len(self.hsmap.keys())



def main():
	lru = LRUCache(1)
	lru.get(1)
	print(lru)
	lru.get(2)
	print(lru)
	lru.get(1)
	print(lru) # 查看顺序是否更新
	lru.get(3)
	print(lru) # 是否删除节点







if __name__ == '__main__':
	main()