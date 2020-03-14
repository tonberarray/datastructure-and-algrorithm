# 霍夫曼树（最优二叉树），霍夫曼编码（前缀编码）
"""路径和路径长度：树中一个节点到另一个的分支连线（边）够成路径，
路径的上连线（边）数目称路径长度，它等于路径上的节点数减1。"""

"""节点的权和带权路径长度：许多应用中，常常将树中的节点赋予一个有着特别意义的实数，
表示该节点保存的数据在总数据集中的频数或占比，我们称此实数为节点的权，
节点的带权路径长度规定以从树的根节点到该节点的路径长度与该节点的权的乘积"""

"""树的带权路径长度（Weighted Path Lenght of Tree,WPL）:
树中所有叶子节点的带权路径长度之和"""

"""霍夫曼树也称为最优二叉树：是由n个带权叶子节点构成的所有二叉树中，
带权路径长度最小的树。"""

"""等长编码：每个字符的编码长度相同
（编码长度就是每个编码字符所含的二进制位数），
编码之后的文件按照固定的长度进行逐一解码，
这种编码的特点是解码简便，每个编码是唯一的，但是编码长度并不是最短的"""

"""前缀编码（prefix code）：为了使文件编码的二进制位数尽可能少，
可以将每个字符的设计为不同长度，使用评率高的字符分配相对较短的编码，
使用评率低的字符分配相对较长的编码，同时还要兼顾编码的唯一性，
即设计编码时必须使任何一个字符编码都不是另一个字符编码的前缀"""

"""当有n个带权的叶子节点时(即前缀编码的数量为n)，
其霍夫曼树的节点数为2n-1"""

class Node(object):
	"""docstring for Node"""
	def __init__(self, data=None, weight=None):
		self.data = data
		self.weight = weight
		self.left = self.right = None


class HaffumanTree(object):
	"""docstring for HaffumanTree"""
	def __init__(self, data_weights):
		self.a =[Node(part[0],part[1]) for part in data_weights]
		while len(self.a) > 1:
			# 根据节点的权值有小到大排序
			self.a.sort(key=lambda node:node.weight, reverse=False)
			weight = self.a[0].weight + self.a[1].weight
			tmp = Node(weight=weight)
			tmp.left = self.a.pop(0)
			tmp.right = self.a.pop(0)
			self.a.append(tmp)
		self.root = self.a[0]
		self.haffumancode = {}
		self.b = [None]*len(data_weights) # 临时存储节点对应的编码

	def prefix_code(self, tree, n):
		"""用递归的思想生成编码"""
		node = tree
		if (not node): # node如果为空则返回
			return
		elif node.data:
			code = ''.join(self.b[:n])
			self.haffumancode[node.data] = code
			# 可以在此输出叶子节点的编码
			# print(f'{node.data}的编码为：', code)
			return
		# 利用前序遍历的逻辑进行编码	
		self.b[n] = '0'
		self.prefix_code(node.left, n+1)
		self.b[n] = '1'
		self.prefix_code(node.right, n+1)

	def haffuman_code(self):
		self.prefix_code(self.root, 0)
		return self.haffumancode



char_weights = [('a',9),('b',12),('c',6),('d',3),('e',5),('f',15)]
tree = HaffumanTree(char_weights)
haffumancode = tree.haffuman_code()
for key,value in haffumancode.items():
	print(f'{key}的编码为:{value}')
		



		