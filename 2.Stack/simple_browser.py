'''
	用链表栈实现浏览器浏览的前进和倒退功能：

	使用两个栈X和Y来分别实现前进和后退功能，首先将浏览过的页面一次性的压入到X栈中；
	当需要倒退操作时，将X栈顶的页面压入到Y栈，当需要前进操作时，将Y栈顶的页面压入到X栈；
	当X栈没有元素时不能再进行倒退操作，当Y栈没有元素时不能再进行前进操作。

	Author by:Lofues
'''
import sys
# 向系统路径中加入link_stack文件
sys.path.append('link_stack.py')
from link_stack import LinkedStack

class Browser(object):
	def __init__(self):
		self._forward = LinkedStack()
		self._back = LinkedStack()

	def open(self,url : str):
		print('open page:{}'.format(url))
		self._back.push(url)

	def can_forward(self) -> bool:
		return False if self._forward.empty() else True

	def can_back(self) -> bool:
		return False if self._back.empty() else True

	def back(self) -> str:
		if not self.can_back():
			print('you can not go back')
			return None
		else:
			url = self._back.top.val
			self._forward.push(self._back.pop())
			print('you go back to the {} page'.format(url))
			return url

	def forward(self) -> str:
		if not self.can_forward():
			print('you can not go forward')
			return None
		else:
			url = self._forward.top.val
			self._back.push(self._forward.pop())
			print('you go forward to the {} page'.format(url))
			return url

def main():
	b = Browser()
	b.open('a')
	b.open('b')
	b.open('c')
	for i in range(4):
		print(b.back())
	print(b.forward())

if __name__ == '__main__':
	main()