# 构建平衡二叉树

class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def height(self, node):
		# 返回计算树的高度
		if node is None:
			return 0
		leftheight = self.height(node.left)
		rightheight = self.height(node.right)	
		return max(leftheight, rightheight) + 1

	def leftheight(self):
		# 返回左子树高度
		return self.height(self.left)	

	def rightheight(self):
		# 返回右子树高度
		return self.height(self.right)

	def leftrotate(self):
		# 树右偏,左旋转
		newnode = Node(self.val)
		newnode.left = self.left
		newnode.right = self.right.left			
		self.val = self.right.val
		self.right = self.right.right
		self.left = newnode

	def rightrotate(self):
		# 树左偏,右旋转
		newnode = Node(self.val)
		newnode.right = self.right
		newnode.left = self.left.right			
		self.val = self.left.val
		self.left = self.left.left
		self.right = newnode

	def add(self, node):
		if node is None:
			return
		if node.val < self.val:
			if self.left is None:
				self.left = node
			else:
				self.left.add(node)
		if node.val > self.val:
			if self.right is None:
				self.right = node
			else:
				self.right.add(node)		 	  	
		"""
		树右偏的条件下有两种可能情况：
		1.以当前树的右子节点为根的树的左子树比以当前树的右子节点为根的树的右子树高。
		2.以当前树的右子节点为根的树的右子树比以当前树的右子节点为根的树的左子树高。
		如果是第1种情况，右子节点先右旋，当前树再左旋。
		如果是第2种情况，当前树左旋
		树的左偏和树的右偏刚好相反，不再赘述
		"""
		# 判断树右偏
		if self.leftheight() - self.rightheight() < -1:
			if self.right.right != None and self.right.leftheight() > self.right.rightheight():
				self.right.rightrotate()
				self.leftrotate()
				return
			else:
				self.leftrotate()
				return
		# 判断树左偏
		if self.leftheight() - self.rightheight() > 1:
			if self.left.left != None and self.left.leftheight() < self.left.rightheight():
				self.left.leftrotate()
				self.rightrotate()
				return
			else:
				self.rightrotate()
				return

class AVLTree(object):
	"""docstring for BinaryTree"""
	def __init__(self):
		self.head = None

	def get_root(self):
		return self.head	

	def createTree(self,vals):
		# 传入一个数组来构造AVL树
		# vals = [5,7,3,1,2,6,8,4,9,0]
		nodes = [Node(val) for val in vals]
		for node in nodes:
			self.add(node)					
		return self.head

	def add(self, node):
		if self.head == None:
			self.head = node
		else:
			self.head.add(node)		

	def searched(self, key):
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

	def delnode(self, key):
		if self.searched(key):
			self.head = self.deletenode(self.head, key)
		else:
			print("节点不存在")
			return 	

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


if __name__ == '__main__':	
	# vals = [5,7,3,1,2,6,8,4,9,0]
	# vals = [4,3,6,5,7,8]
	# vals = [10,12,8,9,7,6]
	vals = [4, 6, 3, 1, 7, 9, 8, 5, 2]

	avl = AVLTree()
	root = avl.createTree(vals)
	avl.travel(root)
	print(root.height(root))
	print(root.leftheight())
	print(root.rightheight())	

