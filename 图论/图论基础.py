# 图形结构，图论，广度优先，深度优先，邻接表

class Vertex:
	def __init__(self, v):
		self.value = v
		self.visited = False
		# 用于保存与其相邻的顶点
		self.adjacentvertaxes = []

	def addadjacentvertaxes(self, vertex):
		self.adjacentvertaxes.append(vertex)

def buildgraph(edges, isDirectional):
	vertexes = {}
	# 先判断顶点集合是否已经有该顶点，如果没有则创建顶点对象
	for edge in edges:
		v1 = vertexes.get(edge[0],None)
		v2 = vertexes.get(edge[1],None)
		if v1 is None:
			v1 = Vertex(edge[0])
			vertexes[edge[0]] = v1
		else:
			v1 = vertexes[edge[0]]

		if v2 is None:
			v2 = Vertex(edge[1])
			vertexes[edge[1]] = v2
			

		if edge[0] == edge[1]:
			continue	
		v1.addadjacentvertaxes(v2)
		vertexes[edge[0]] = v1
		"""
		如果是无向图，v1与v2相邻，v2与v1也相邻
		如果是有向图，v1与v2相邻不一定代表v2与v1相邻
		"""
		if isDirectional is False:
			v2.addadjacentvertaxes(v1)
			vertexes[edge[1]] = v2
	return vertexes


def DepthFirstSearch(vertex):
	"""深度优先"""
	if vertex.visited is True:
		return
	vertex.visited = True
	for v in vertex.adjacentvertaxes:
		print('{0}-->{1}'.format(vertex.value, v.value))
		DepthFirstSearch(v)
	

def breadthFirstSearch(vertex):
	""""广度优先"""
	if vertex.visited is True:
		return
		
	vertex.visited = True
	for v in vertex.adjacentvertaxes:
		print('{0}-->{1}'.format(vertex.value,v.value))

edges = [[1,2],[1,5],[5,9],[9,10],[5,10],[6,6],[3,4],\
[3,7],[7,11],[7,8],[3,8],[4,8],[11,8],[8,12]]

graph = buildgraph(edges,True)
for node in graph.values():
	DepthFirstSearch(node)
print('*'*20)	

for node in graph.values():
	node.visited = False
for node in graph.values():
	breadthFirstSearch(node)

def bfs(vertex): # 函数只适用于全连通图
	visited = []
	queue = [vertex]
	visited = append(vertex.value)
	while queue:
		cur = queue.pop(0)
		for x in cur.adjacentvertaxes:
			if x.value not in visited:
				visited.append(x.value)
				queue.append(x)
	return visited
	

def dfs(vertex):  # 函数只适用于全连通图
	stack = [vertex]
	visited = []
	while stack:
		cur = stack.pop()
		if cur.value not in visited:
			visited.append(cur.value)
		for x in cur.adjacentvertaxes:
			if x.value not in visited:
				stack.append(x)
	return visited			
