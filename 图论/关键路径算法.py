# 关键路径


"""AOE(Activity on Edge Network)网：
一个表示工程的带权有向图中，
顶点表示事件，有向边表示活动，
边上的权值表示活动持续时间，
这种有向图的边表示活动的网，就是AOE网"""

"""etv(earlist time of vertex):
事件最早发生时间，顶点最早发生的时间"""

"""ltv(latest time of vertex):
事件最晚发生时间，每个顶点对应的最晚需要开始的时间
如果超过此时间，将延误整个工期"""

"""ete(earlist time of edge):
活动最早发生时间，弧最早发生的时间"""

"""lte(latest time of edge):
活动最晚发生时间，不推迟工期最晚的开工时间"""

"""关键路径： 
AOE网中从起始事件（源点）到终事件(汇点)耗时最长的路线，
这条路线的长为工程的工期"""
def creategraph(edges, isdirectional):
	"""边集数组，以[tail,head,weight]存储数据"""
	vertexes = {}
	for edge in edges:
		v1 = vertexes.get(edge[0], None)
		v2 = vertexes.get(edge[0], None)
		if v1 is None:
			vertexes[edge[0]] = []
			v1 = []
		if v2 is None:
			vertexes[edge[1]] = []
			v2 = []

		if edge[0] == edge[1]:
			continue

		v1.append([edge[1], edge[2]])
		vertexes[edge[0]] = v1
		if (not isdirectional):
			v2.append([edge[0], edge[2]])
			vertexes[edge[1]] = v2

	return vertexes


def topological_sort(graph):
	num = len(graph)
	# 先初始化所有顶点入度为0,顶点事件最早发生时间etv为0,
	etv = dict((i,0) for i in graph)
	in_degree = dict((i, 0) for i in graph)
	for x in graph:	
	 	for v in graph[x]:
	 		in_degree[v[0]] += 1
	stack = [v for v in in_degree if in_degree[v] == 0]
	top_sort = []
	
	while stack:
		v = stack.pop()
		top_sort.append(v)
		for i in graph[v]:
			in_degree[i[0]] -= 1
			if in_degree[i[0]] == 0:
				stack.append(i[0])
			if i[1] + etv[v] > etv[i[0]]:
				etv[i[0]] = i[1] + etv[v]
	# 如果有环，返回错误。
	# 如果拓扑排序没问题，返回	拓扑序列和顶点事件最早发生时间			
	if len(top_sort) == num:
		return top_sort, etv
	else:
		return False			
		

def criticalpath(graph):
	if not topological_sort(graph):		
		raise Exception('the graph is a circle')
	top_sort, etv = topological_sort(graph)
	print(etv)
	# 取终点的事件最早发生时间
	end = max(etv.values()) 
	# end = etv[top_sort[-1]]
	# 初始化所有顶点事件的最迟发生时间为终点的事件最早发生时间
	ltv = dict((i, end) for i in graph)
	while top_sort:
		vertex = top_sort.pop()
		for v in graph[vertex]:
			if ltv[v[0]] - v[1] < ltv[vertex]:
				ltv[vertex] = ltv[v[0]] -v[1]
	print(ltv)			
	for vertex in graph:
		for v in graph[vertex]:
			ete = etv[vertex]
			lte	= ltv[v[0]] - v[1]
			# 关键路径输出
			if ete == lte:
				print(f'tail:{vertex} head:{v[0]} weight:{v[1]}')
		

# edges = [['A','B'],['A','C'],['D','C'],
# 	['D','E'],['B','F'],['C','F'],['C','G'],
# 	['E','G'],['F','H'],['G','H'],
# 	['G','I'],['H','J'],['I','J']]
edges = [['A','B',6],['A','C',4],['A','D',4],
	['B','E',2],['C','E',2],['C','F',1],['D','G',3],
	['E','H',3],['F','H',2],['F','I',4],
	['G','I',4],['H','J',2],['I','J',2]]

edges2 = [['A','B',6],['A','C',4],['A','D',5],
	['B','E',1],['C','E',1],['D','F',2],['E','G',7],
	['E','H',5],['F','H',4],['H','I',4],
	['G','I',2]]	

graph = creategraph(edges2,True)
criticalpath(graph)
	
