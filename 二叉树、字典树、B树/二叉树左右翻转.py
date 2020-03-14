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
			return None
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
		return None


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


def horizontallyFlip(root):
	# 二叉树左右翻转，层序遍历到树每个节点
	if root == None:
		print("传入的树为空")
		return
	nodes = []
	nodes.append(root)

	while nodes:
		cur = nodes[0]
		del(nodes[0])
		# 左右翻转
		cur.left, cur.right = cur.right, cur.left
		if cur.left is not None:
			nodes.append(cur.left)
		if cur.right is not None:
			nodes.append(cur.right)

	return root		



tree = BinaryTree()
head = tree.createBiTree()
tree.travel(head)
root = horizontallyFlip(head)
tree.travel(root)