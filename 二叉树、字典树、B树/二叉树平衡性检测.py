# 二叉排序树， 以队列方式对树结构进行层序遍历

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

	def travel(self, head):
		"""以队列方式对树结构进行逐层遍历"""
		if head is None:
			print('None')
		nodes = []
		nodes.append(head)

		while len(nodes) > 0:
			tmp = nodes[0]
			nodes.pop(0)

			print(f"{tmp.val}",end=' ')
			if tmp.left is not None:
				nodes.append(tmp.left)
			if tmp.right is not None:
				nodes.append(tmp.right)
		print('')	


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


def leveltravel(head):
	"""层序遍历"""
	if head is None:
		return []
	data = []
	level = [head]
	while level:
		nextlevel = []
		data.append([node.val for node in level])
		for node in level:
			if node.left:
				nextlevel.append(node.left)	
			if node.right:
				nextlevel.append(node.right)
		level = nextlevel			
	return data
	

# 判断是否为平衡二叉树
class BalencedTree(object):
	"""docstring for BalencedTree"""
	def __init__(self):
		self.balenced = True

	def isbalenced(self, root):
		self.cumputeTreeheight(root)
		return self.balenced

	def cumputeTreeheight(self, root):
		if root is None:
			return 0
		# 计算左右子树的高	
		leftheight = self.cumputeTreeheight(root.left)
		rightheight = self.cumputeTreeheight(root.right)
		if abs(leftheight -	rightheight) > 1:
			self.balenced = False

		height = 0
		if leftheight > rightheight:
			height = leftheight
		else:
			height = rightheight
		print(f'node:{root.val}, leftheight:{leftheight}, rightheight:{rightheight},height:{height+1}')
		return height + 1
						

vals = [6,4,9,2,5,7,10,1,3,8]
tree = Tree()
head = tree.createTree(vals)
tree.travel(head)
bt = BalencedTree()
isbalenced = bt.isbalenced(head)
mid = inorder(head)	
print(mid)	
print(isbalenced)	
