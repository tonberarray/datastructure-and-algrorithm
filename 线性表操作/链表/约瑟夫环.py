# 约瑟夫问题
""" 犹太历史学家Josephus经历：罗马人占领乔塔帕特后，
39个犹太人与Josephus和他的朋友躲在一个洞里，
39个犹太人宁杀也不愿被抓，于是决定采用自杀方式，
41个人拍一个圈，第1人开始报数每报数到第3人，此人必须自杀，
然后下一个重新报数，直到所有人都自杀为止,
Josephus和他的朋友不想自杀，和他的朋友暗中商量，
先假装遵从，他和朋友站在第16位和31位，
成为最后两个人自杀的人，于是逃过了这死亡游戏"""

class Node(object):
	"""docstring for Node"""
	def __init__(self, val=None):
		self.val = val
		self.next = None
		
class LinkList(object):
	"""docstring for LinkList"""
	def __init__(self):		
		self.head = None
						
	def creatList(self, num):					
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
				node.next = node
				head = node
				cur = head
			else:
				node.next = head
				cur.next = node
				cur = cur.next
			val += 1
			num -= 1	

		self.head = head
		return head 	

	def travel(self, head):
		"""遍历链表"""	
		if isinstance(head, Node) == False:
			print('error: This arguement is invalid')
			return
		if head is None:
			print('None')
			return
		cur = head 
		while cur.next != head:
			print(f'{cur.val}', end=' ')
			cur = cur.next
		print(f'{cur.val}')

	def josephus(self, num, m):
		"""死亡游戏"""	
		head = self.creatList(num)
		cur = head
		if m == 1:
			self.travel(head)

		while cur != cur.next:
			for i in range(m-2):
				cur = cur.next
			print(f'{cur.next.val}->', end='')
			cur.next = cur.next.next
			cur = cur.next
			# 另一种写法
			# tmp = cur.next
			# cur.next = tmp.next	
			# cur = cur.next
		print(f'{cur.val}')	

	def josephus2(self, num):
		"""死亡游戏"""	
		head = self.creatList(num)
		cur = head
		m = cur.val
		while cur != cur.next:
			if m == 1:
				print(f'{cur.val}->',end='')
				m = cur.val
				p = head
				while p.next != head:
					p = p.next
				head = head.next
				p.next = head 	
				cur = cur.next
			else:
				for i in range(m-2):
					cur = cur.next
				print(f'{cur.next.val}->', end='')
				m = cur.next.val
				cur.next = cur.next.next
				cur = cur.next
				# 另一种写法
				# tmp = cur.next
				# cur.next = tmp.next	
				# cur = cur.next
		print(f'{cur.val}')


l = LinkList()
head = l.creatList(1)
l.travel(head)
l.josephus(41,3)
l.josephus2(41)
		
		