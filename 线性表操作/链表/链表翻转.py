class Node:
	def __init__(self, val):
		self.next = None
		self.val = val


class ListUtility:
	def __init__(self):
		self.head = None
		self.tail = None
		pass
		
	def createList(self,nodeNum):
		#生成含有nodeNum个节点的列表
		if nodeNum <= 0:
			return None
		head = None
		val = 0
		node = None
		
		#构造给定个节点数的队列，每个节点数值依次递增
		while nodeNum > 0:
			'''
			如果head指针为空，代码先构造队列头部。如果不为空，代码构造节点对象。
			然后用上一个节点的next指针指向当前节点，从而将多个节点串联形成队列。
			'''
			if  head is None:
				head = Node(val)
				node = head
			else:
				node.next = Node(val)
				node = node.next
				self.tail = node
			val += 1
			nodeNum -= 1
			
		self.head = head
		
		return head
	
	def printList(self,head):
		'''
		根据队列头结点，依次遍历队列每个节点对象，并打印出节点值
		假设队列含有三个节点，节点值分别为1，2，3，那么代码输出结果为：
		1->2->3->null
		'''
		while head != None:
			print("{0}->".format(head.val), end="")
			head = head.next
		print("null")

	def reverse_list1(self, head):
		# 链表翻转（递归）
		if head == None or head.next == None:
			return head
		else:
			new_head = self.reverse_list1(head.next)
			head.next.next = head
			head.next = None
			return new_head

	def reverse_list2(self, head):
		# 链表翻转（迭代）
		new_head = None
		while head != None:
			cur = head.next
			head.next = new_head
			new_head = head
			head = cur
		return new_head


utility = ListUtility()
head = utility.createList(10)
utility.printList(head)
new_head = utility.reverse_list2(head)
utility.printList(new_head)	
print(new_head.val)		