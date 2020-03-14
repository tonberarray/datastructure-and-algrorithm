# 单链表及其节点的增删查改


class Node(object):
	"""docstring for Node"""
	def __init__(self, val=None):
		self.item = val
		self.next = None


class LinkList(object):
	"""docstring for LinkList"""
	def __init__(self):
		self.head = None
		self.tail = None

	def size(self):
		if self.head == None:
			return 0 
		count = 0
		p = self.head
		while p:
			p = p.next
			count += 1
		return count	

	def add(self, val):
		"""头插法"""
		if isinstance(val, Node):
			node = val
		else:
			node = Node(val)	

		node.next = self.head
		self.head = node

	def append(self, val):
		"""尾插法"""
		if isinstance(val, Node):
			node = val
		else:
			node = Node(val)	

		if self.head == None:
			self.head = node
			self.tail = node
		else: 
			p = self.head
			while p.next:
				p = p.next
			p.next = node
			self.tail = node
	
	def insert(self, index, val):		
		if index >= self.size():
			self.append(val)
		elif index <= 0:
			self.add(val)
		else:
			node = Node(val)
			p = self.head
			count = 1
			while count < index:
				p = p.next
				count += 1
			node.next = p.next
			p.next = node
			# tmp = p.next
			# p.next = node
			# node.next = tmp			

	def travel(self):
		"""链表遍历"""
		if self.head == None:
			print('None')
			return

		cur = self.head
		while cur:
			print('{0}->'.format(cur.item),end='')
			cur =cur.next
		print('None')

	def delete(self, index):
		if self.head == None:
			print('this list is empty')
			return 	 							
		elif index < 0 or index >= self.size():
			print('error:out of index')
			return
		elif index == 0:
			self.head = self.head.next
			return	
		else:
			p = self.head
			count = 1
			while count < index:
				p = p.next
				count += 1
			tmp = p.next
			p.next = tmp.next
			# p.next = p.next.next
			# p = p.next
			return

	def allclear(self):
		self.head = None
		self.tail = None				
	
	def get(self, index):
		if self.head == None:
			print('this list is empty')
			return 	 							
		elif index < 0 or index >= self.size():
			print('error:out of index')
			return
		else:
			p = self.head
			count = 0
			while count < index:
				p = p.next
				count += 1
			return p.item	

	def alter(self, index,val):
		if self.head == None:
			print('The list is empty')
			return 	 							
		elif index < 0 or index >= self.size():
			print('error:out of index')
			return
		else:
			p = self.head
			count = 0
			while count < index:
				p = p.next
				count += 1
			p.item = val
			return

	def search(self,val):
		"""查找元素是否存在"""
		cur = self.head
		while cur:
			if cur.item == val:
				return True
			cur = cur.next
		return False

def creatList(nodeNum):
	"""创建一个0到nodeNum-1的链表"""	
	if isinstance(nodeNum, int) == False:
		print("error: not type:int")
		return
	
	l = LinkList()	
	if nodeNum <= 0:
		return l

	val = 0
	while nodeNum > 0:
		l.append(val)
		val += 1
		nodeNum -= 1

	return l	


def connect(l1, l2):
	"""两个链表首尾串联"""
	while isinstance(l1, LinkList)	and isinstance(l2, LinkList):
		p = l1.tail
		p.next = l2.head
		l1.tail = l2.tail
		return l1
		


l1 = creatList(15)
l2 = creatList(15)
l = connect(l1,l2)
l.travel()
print(l.size())
