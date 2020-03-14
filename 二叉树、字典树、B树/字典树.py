# 字典树

class Node(object):
	"""docstring for Node"""
	def __init__(self):
		self.string = ''
		self.map = {}

	def setString(self, string):
		"""设置节点对应的字符串"""
		self.string = string

	def getString(self):
		return self.string

	def nextNode(self, b):
		"""根据字符构造子节点"""
		if self.map.get(b) is None:
			n = Node()
			self.map[b] = n	
		return self.map[b]

	def getNode(self, b):
		"""根据字符返回当前节点对应的子节点"""
		return self.map[b]

	def getAllNextNodes(self):
		arr = []
		begin = ord('z')
		end = ord('a') - 1
		for i in range(begin, end, -1):
			n = self.map.get(chr(i))
			if n:
				arr.append(n)
		return arr


class Trie(object):
	"""docstring for Trie"""
	def __init__(self):
		self.root = Node()
		self.stack = []

	def addword(self,string):
		node = self.root 
		for i in range(len(string)):
			node = node.nextNode(string[i])

		node.setString(string)	

	def addNodelistTostack(self, nodes):
		for node in nodes:
			self.stack.append(node)

	def getAllWordsByPrefix(self, prefix):
		node = self.root
		for i in range(len(prefix)):
			node = node.getNode(prefix[i])
			if node is None:
				return 
		self.addNodelistTostack(node.getAllNextNodes())
		allwords = []
		while self.stack:
			n = self.stack.pop()
			if n.getString():
				allwords.append(n.getString())
			self.addNodelistTostack(n.getAllNextNodes())

		return allwords


dictionary = {'tea','to','ted','A','ten','in','inn'}
trie = Trie()
for  word in dictionary:
	trie.addword(word)
prefixwords = trie.getAllWordsByPrefix('t')
print('words with prefix of "t" are:')
for word in prefixwords:
	print(word,end=' ')	
print('')	
						