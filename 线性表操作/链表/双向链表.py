# dual_link_List 双向链表


class DualNode(object):
	"""docstring for DualNode"""
	def __init__(self, val=None):

		self.val = val
		self.prior = None
		self.next = None
		self.visited = False


class DualLinkList(object):
	"""docstring for DualLinkList"""
	def __init__(self):
		self.head = None

	def createList(self,num):
		"""创建num个节点的双向链表"""
		if isinstance(num, int) == False:
			print("error: not type:int")
			return
		if num <=0:
			return None

		head = None
		val = chr(65)
		cur = None
		n = 0
		while num > 0:
			val = chr(65 + n)
			node = DualNode(val)
			if head is None:
				head = node
				cur = head
			else:
				node.next = cur.next
				node.prior = cur
				cur.next = node
				cur = cur.next
			n += 1
			num -= 1
		self.head = head
		return head

	def createCircleList(self, num):
		"""创建num个节点的双向循环链表"""
		if isinstance(num, int) == False:
			print("error: not type:int")
			return
		if num <=0:
			return None

		head = None
		val = chr(65)
		cur = None
		n = 0
		while num > 0:
			val = chr(65 + n)
			node = DualNode(val)
			if head is None:
				head = node
				cur = head
			else:
				node.next = cur.next
				node.prior = cur
				cur.next = node
				cur = cur.next
			n += 1
			num -= 1
		cur.next = head
		head.prior = cur	
		self.head = head
		return head
			
	def travel(self, head):
		"""遍历链表"""	
		if isinstance(head, DualNode) == False:
			print('error: This arguement is invalid')
			return
		if head is None:
			print('None')
			return
		cur = head 
		while cur.next != head and cur.next != None:
			print(f'{cur.val}', end='')
			cur = cur.next
		print(f'{cur.val}')

	def caesar(self,n):
		"""Caesar Code加密模式"""
		if isinstance(n, int) == False:
			print("error: not type:int")
			return
		
		head = self.createCircleList(26)	
		if n == 0:
			self.travel(head)
		elif n < 0:
			m = n
			while m < 0:
				head = head.prior
				m += 1
			self.travel(head)
		else:
			for _ in range(n):
				head = head.next
			self.travel(head)		


l = DualLinkList()
head = l.createCircleList(26)
l.travel(head)
l.caesar(-3)
print(len('13'))

# a = chr(65)
# m = ord('A')
# print(a,m)