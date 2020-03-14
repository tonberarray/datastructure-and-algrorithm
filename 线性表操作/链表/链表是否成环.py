# 链表


class Node(object):
	"""docstring for Node"""
	def __init__(self, val=None):
		self.val = val
		self.next = None
		# 避免成遍历时成死循环
		self.visited = False 

		
class LinkList(object):
	"""docstring for LinkList"""
	def __init__(self):		
		self.head = None
		self.rear = None
						
	def createList(self, num):					
		"""创建一个1到num的链表"""	
		if isinstance(num, int) == False:
			print("error: not type:int")
			return
		
		if num <= 0:
			return None

		head = None
		val = 1
		cur = None # 游标指向最后一个节点
		while num > 0:
			node = Node(val)
			if head is None:
				head = node
				cur = head
			else:
				cur.next = node
				cur = cur.next
				self.rear = node
			val += 1
			num -= 1	

		self.head = head
		return head

	def createCycleList(self, num):					
		"""创建一个1到num的循环链表"""	
		if isinstance(num, int) == False:
			print("error: not type:int")
			return
		
		if num <= 0:
			return None

		head = None
		val = 1
		cur = None # 游标指向最后一个节点
		while num > 0:
			node = Node(val)
			if head is None:
				head = node
				cur = head
			else:
				cur.next = node
				cur = cur.next
				self.rear = node
			val += 1
			num -= 1
		p = head	
		for _ in range(2):
			p = p.next
		cur.next = p	
		self.head = head
		return head	 	

	def travel(self, head):
		"""遍历链表"""	
		if isinstance(head, Node) == False:
			print('error: This arguement is invalid')
			return
		if head is None:
			print('None')

		cur = head 
		while cur and cur.visited == False:
			print(f'{cur.val}', end=' ')
			cur.visited = True
			cur = cur.next
		print('')

	def iscycle(self, head):
		"""判断单向链表内部是否有环"""
		p = head
		cur  = head
		while p and cur and p.next and \
		cur.next and cur.next.next:
			p = p.next
			cur = cur.next.next
			if p == cur:
				return True
		return False	


l = LinkList()
head = l.createList(10)
print(l.iscycle(head))		