# 二叉排序树及其遍历
 
class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BinaryTree(object):
	"""docstring for BinaryTree"""
	def __init__(self):
		self.head = None

	def createBiTree(self):
		vals = [5,7,3,1,2,6,8,4,9,0]
		for val in vals:
			self.add(val)
		return self.head
	
	def add(self, val):
		if self.head == None:
			self.head = Node(val)
			return
		cur = self.head	
		while cur != None:
			if cur.val > val and cur.left is not None:
				cur = cur.left
				continue
			if cur.val <= val and cur.right is not None:
				cur = cur.right
				continue
			node = Node(val)
			if cur.val > val:
				cur.left = node
				break
			else:
			 	cur.right = node
			 	break

	def search(self, key):
		"""查找元素是否存在"""
		if self.head is None:
			return False
		cur = self.head
		while cur != None:
			if cur.val > key: 
				cur = cur.left
				continue
			if cur.val < key:
				cur = cur.right
				continue	
			if cur.val == key:
				return True	
		return False


	def deletenode(self, head, val):
		"""删除节点"""
		if not head:
			return
		if head:
			if val < head.val:
				head.left = self.deletenode(head.left, val)
			elif val > head.val:
				head.right = self.deletenode(head.right, val)
			elif head.left and head.right:
				cur = head.left
				while cur.right:
					cur = cur.right
				head.val = cur.val
				head.left = self.deletenode(head.left, head.val)
			elif head.left is None:
				head = head.right
			elif head.right is None:
				head = head.left				
		return head		

	def travel(self, head):
		"""以队列方式对树结构进行层序遍历"""
		if head is None:
			print('None')
		nodes = []
		nodes.append(head)

		while len(nodes) > 0:
			tmp = nodes[0]
			del(nodes[0])

			print(f"{tmp.val}",end=' ')
			if tmp.left is not None:
				nodes.append(tmp.left)
			if tmp.right is not None:
				nodes.append(tmp.right)
		print('')



def pretravel(tree):
	"""前序遍历"""
	if tree == None:
		return
	print(tree.val, end=' ')
	pretravel(tree.left)
	pretravel(tree.right)					


def midtravel(tree):
	"""中序遍历"""
	if tree == None:
		return	
	midtravel(tree.left)
	print(tree.val, end=' ')
	midtravel(tree.right)


def aftertravel(tree):
	"""后序遍历"""
	if tree == None:
		return	
	aftertravel(tree.left)
	aftertravel(tree.right)
	print(tree.val, end=' ')


def preorder(head):
	"""借助栈的特点对二叉树进行前序遍历，非递归"""
	if head is None:
		return []
	data = []
	stack = [head]
	while stack:
		cur = stack.pop()
		if cur:
			data.append(cur.val)
			stack.append(cur.right)
			stack.append(cur.left)		
	return data 


def inorder(head):
	"""借助栈的特点对二叉树进行中序遍历，非递归"""
	if head is None:
		return []
	data = []
	stack = []	
	cur = head
	while cur or stack:
		if cur:
			stack.append(cur)
			cur = cur.left
		else:
			cur = stack.pop()
			data.append(cur.val)
			cur = cur.right
	return data


def postorder(head):
	"""借助栈的特点对二叉树进行后序遍历，非递归"""
	if head is None:
		return []	
	data = []	
	stack = [head] 
	while stack:
		cur = stack.pop()
		if cur:
			data.append(cur.val)
			stack.append(cur.left)
			stack.append(cur.right)
	return data[::-1] 		


tree = BinaryTree()
head = tree.createBiTree()
tree.travel(head)
pretravel(head)
print('')
midtravel(head)
print('')
aftertravel(head)
print('')
m = ['9','2','1','2','6']		
print(''.join(m))

head = tree.deletenode(head,3)
tree.travel(head)
pretravel(head)
print('')
midtravel(head)
print('')
print(tree.search(10))