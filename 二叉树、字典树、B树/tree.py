# 树形结构

# 第一种 双亲表示
class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.parent = None


class ParnetTree(object):
	"""docstring for ParnetTree"""
	def __init__(self):
		self.root = []
		self.size = 0
		
	def createTree(self,vals):
			pass	

# 第二种 子树表示，需要先考虑树的度确定子树的个数
class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.child1 = None
		self.child2 = None
		self.child3 = None


class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		self.root = None
		self.size = 0
		
	def createTree(self,vals):
			pass				

# 第三种
class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.nextchild = None

class First(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.parent = None
		self.firstchild = None


class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		self.root = []
		self.size = 0
																		