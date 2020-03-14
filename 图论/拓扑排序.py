# 拓扑排序（无环路径的有向图能够形成拓扑排序）
"""拓扑排序的特点是前面的元素指向后面的元素，后面的元素不能只向前面的元素"""



def creategraph(edges, isdirectional):
	
	vertexes = {}
	for edge in edges:
		v2 = vertexes.get(edge[0], None)
		if v1 is None:
			vertexes[edge[0]] = set()
			v1 = set()
		if v2 is None:
			vertexes[edge[1]] = set()
			v2 = set()

		if edge[0] == edge[1]:
			continue

		v1.add(edge[1])
		vertexes[edge[0]] = v1
		if (not isdirectional):
			v2.add(edge[0])
			vertexes[edge[1]] = v2

	return vertexes


def topological_sort(graph):
	num = len(graph)
	# 先初始化所有顶点入度为0
	in_degree = dict((i, 0) for i in graph)
	for x in graph:	
	 	for v in graph[x]:
	 		in_degree[v] += 1
	stack = [v for v in in_degree if in_degree[v] == 0]
	top_sort = []
	
	while stack:
		v = stack.pop()
		top_sort.append(v)
		for i in graph[v]:
			in_degree[i] -= 1
			if in_degree[i] == 0:
				stack.append(i)
	if len(top_sort) == num:
		return top_sort	
	else:			
		raise Exception('the graph is a circle')

edges = [['A','B'],['A','C'],['D','C'],
	['D','E'],['B','F'],['C','F'],['C','G'],
	['E','G'],['F','H'],['G','H'],
	['G','I'],['H','J'],['I','J']]

	
graph = creategraph(edges, True)
seq = topological_sort(graph)

print(seq)
