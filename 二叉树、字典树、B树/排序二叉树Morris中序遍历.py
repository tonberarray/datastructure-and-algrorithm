# 二叉排序树Morris中序遍历

class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		self.head = None

	def createTree(self, vals):
		for val in vals:
			self.insertNode(val)
		return self.head
	
	def insertNode(self, val):
		
		if self.head is None:
			self.head = Node(val)
			return
		cur = self.head	
		while cur is not None:
			# 插入节点的值小于当前节点值，放在左子树
			if cur.val > val and cur.left is not None:
				cur = cur.left
				continue
			# 插入节点的值大于当前节点值，放在右子树
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


class MorrisTravel(object):
	"""docstring for MorrisTravel"""
	def __init__(self, root):
		self.root = root
	def travel(self):
		node = self.root
		while node:
			if node.left is None:
				print(node.val, end=' ')
				node = node.right
			else:
				pre = self.getpredecessor(node)
				if pre.right is None:
					pre.right = node
					node = node.left
				elif pre.right is node:
					pre.right = None
					print(node.val, end=' ')
					node = node.right	

	def getpredecessor(self, node):
		pre = node
		if node.left:
			pre = pre.left
			while pre.right and pre.right is not node:
				pre = pre.right
		return pre
		
vals = [6,4,9,2,5,7,10,1,3,8]
tree = Tree()
head = tree.createTree(vals)
mt = MorrisTravel(head)
mt.travel()
print('')