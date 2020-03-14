# 循环链表解决拉丁方阵问题
"""拉丁方正:将n个不同值的元素填在n×n的表格方阵里，
使得这n个元素在方阵的每一行每一列都只出现一次"""


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

	def latin_matrix(self,num):
		if isinstance(num, int) == False and num <= 0:
			print('error: This arguement is invalid')
			return
		head = self.creatList(num)
		print('拉丁方阵如下：')
		while num > 0:
			self.travel(head)
			head = head.next
			num -= 1


def latinmatrix(num):
	"""列表版拉丁方阵"""
	if isinstance(num, int) == False and num <= 0:
		print('error: This arguement is invalid')
		return
	latin =	[x for x in range(1,num+1)]
	n = num
	print('列表拉丁方阵如下：')
	while n > 0:
		print(latin)
		tmp = latin[0]
		latin.append(tmp)
		latin =latin[1:]
		n -= 1

# l = LinkList()
# l.latin_matrix(9)
latinmatrix(9)