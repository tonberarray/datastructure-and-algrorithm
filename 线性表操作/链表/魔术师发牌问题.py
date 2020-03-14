# 魔术师发牌问题
"""13张黑桃，魔术师发牌时不看牌面，总是能知道牌的点数。
扑克牌事先按照一定顺序排好，开始数牌，
第一张是1（黑桃A），牌面放到桌上，
然后往下数时，最上面的牌放在牌堆最下面，
数到二，牌面为2，放到桌上，
如此循环，直到最后一张13（黑桃K）"""


class Node(object):
	"""docstring for Node"""
	def __init__(self, val=None):
		self.val = val
		self.next = None
		self.visited = False
		
class LinkList(object):
	"""docstring for LinkList"""
	def __init__(self):		
		self.head = None
						
	def creatList(self, num=13):					
		"""循环链表初始化"""	
		if isinstance(num, int) == False:
			print("error: not type:int")
			return
		
		if num <= 0:
			return None

		val = 0
		head = Node(val)
		cur = head
		while num > 1:
			cur.next = Node(val)
			cur = cur.next
			num -=1	
		cur.next = head
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
		while cur.visited == False:
			print(f'{cur.val}', end=' ')
			cur.visited = True
			cur = cur.next
		print('')	
	#	print(f'{cur.val}')

	def magician_poker(self,num):
		"""魔术师扑克排序的实现"""
		head = self.creatList(num)
		cur = head
		cur.val = 1
		for cardcount in range(2,num+1):
			n = 0
			while n < cardcount:
				cur = cur.next
				if cur.val == 0:
					n += 1
			cur.val = cardcount	
		return head


def magicianpoker(num):
	"""列表实现魔术师扑克排序"""
	
	# 初始化列表
	card_list = [0]*num
	for cardcount in range(1,num+1):
		n = 0
		while n < cardcount:
			tmp = card_list[:1]
			card_list.extend(tmp)
			card_list = card_list[1:]
			if card_list[0]	== 0:
				n += 1						
		card_list[0] = cardcount
	first = [i for i in range(num) if card_list[i] == 1]
	first = first[0]
	temp = card_list[:first]
	card_list.extend(temp)
	card_list = card_list[first:]

	return card_list


def magicianpoker2(n):
	v_l = [1]*n                ## 初始化存储数值
	l = list(range(1,n+1))     ## 初始化地址数值
	i = 0                      ## 标记数数的次数，初始化为0
	pos = 1

	while len(l)>=1:        
		i = i+1
		if i == pos:
			v_l[l[0]-1] = pos
			l = l[1:]
			pos = pos+1
			i = 0
		else:
			temp = l[:1]
			l.extend(temp)
			l = l[1:]
	print(str(n)+'张牌的排列顺序为' ,v_l) 

l = LinkList()
head = l.magician_poker(15)
l.travel(head)
cards = magicianpoker(15)
print(cards)
