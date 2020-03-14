# 循环单链表


class Node(object):
	"""docstring for Node"""
	def __init__(self, val=None):
		self.item = val
		self.next = None


class CycleSingleList(object):
	"""docstring for LinkList"""
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def add(self, val):
		"""头插法"""
		if isinstance(val, Node):
			node = val
		else:
			node = Node(val)	

		if self.length == 0:
			node.next = node
			self.head = node
			self.tail = node
		else:
			cur = self.head
			while cur.next != self.head:
				cur = cur.next
			node.next = self.head
			cur.next = node
			self.tail = cur
			self.head = node
		self.length += 1		

	def append(self, val):
		"""尾插法"""
		if isinstance(val, Node):
			node = val
		else:
			node = Node(val)	

		if self.length == 0:
			node.next = node
			self.head = node
			self.tail = node
		else: 
			p = self.head
			while p.next != self.head:
				p = p.next
			node.next = self.head	
			p.next = node
			self.tail = node
		self.length += 1
	
	def insert(self, index, val):		
		if index >= self.length:
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
			self.length += 1
			

	def travel(self):
		"""链表遍历"""
		if self.length == 0:
			print('None')
			return

		cur = self.head
		while cur.next != self.head:
			print('{0}'.format(cur.item),end=' ')
			cur = cur.next
		print('{0}'.format(cur.item))

	def delete(self, index):
		if self.length == 0:
			print('this list is empty')
			return 	 							
		elif index < 0 or index >= self.length:
			print('error:out of index')
			return
		elif index == 0:
			cur = self.head
			while cur.next != self.head:
				cur = cur.next
			self.head = self.head.next
			cur.next = self.head
			self.length -= 1
			return	
		else:
			p = self.head
			count = 1
			while count < index:
				p = p.next
				count += 1
			tmp = p.next
			p.next = tmp.next
			# 另一种写法
			# p.next = p.next.next
			# p = p.next
			self.length -= 1
			return

	def allclear(self):
		self.head = None
		self.length = 0 
	
	def get(self, index):
		if self.length == 0:
			print('this list is empty')
			return 	 							
		elif index < 0 or index >= self.length:
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
		if self.length == 0:
			print('The list is empty')
			return 	 							
		elif index < 0 or index >= self.length:
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
		while cur.next != self.head:
			if cur.item == val:
				return True
			cur = cur.next
		if cur.item == val:
			return True	
		return False

def creatList(nodeNum):
	"""创建一个1到nodeNum的链表"""	
	if isinstance(nodeNum, int) == False:
		print("error: not type:int")
		return
	
	l = CycleSingleList()	
	if nodeNum <= 0:
		return l

	val = 1
	while nodeNum > 0:
		l.append(val)
		val += 1
		nodeNum -= 1

	return l

def connect(l1, l2):
	"""两个循环链表首尾串联"""
	while isinstance(l1, CycleSingleList) and isinstance(l2, CycleSingleList):
		p = l1.tail.next
		l1.tail.next = l2.tail.next
		l2.tail.next = p
		l1.length += l2.length
		return l1


l1 = creatList(15)
l1.travel()
l2 = creatList(12)
l2.travel()
l = connect(l1,l2)
l.travel()
print(l.length)
