# 最小生成树（Prim算法）

MAX = float('inf') # 定义无穷大

def prim_tree(num, matrix): 
	"""邻接矩阵，Prim算法求解图的最小生成树"""
	primtree = {}
	minweight = [0]
	Sum = 0
	# neighbours[k]保存的值为与下标为k的顶点距离最近(权值最小)的顶点的下标值
	# neighbours数组在这里的用途有点类似于KMP算法中的next数组
	neighbours = [0] 
	for i in range(1,num):
		neighbours.append(0)
		minweight.append(matrix[0][i])
	for _ in range(1,num):
		min_weight = MAX
		k = 0
		for x in range(1,num):
			if minweight[x] != 0 and minweight[x] < min_weight:
				k = x
				min_weight = minweight[x]
		primtree[(neighbours[k],k)]= min_weight
		Sum += min_weight
		minweight[k] = 0
			
		for j in range(1,num):
			if minweight[j] != 0 and matrix[k][j] < minweight[j]:
				minweight[j] = matrix[k][j]
				neighbours[j] = k
				
	return primtree, Sum

# 在边集数组edges中边的形式为[tail,head,weight]
def kruskal_tree(vertexes,edges):
	"""边集数组，Kruskal算法求解图的最小生成树"""
	kruskal = []
	edges.sort(key=lambda edge:edge[2])
	Sum = 0 # 保存最小生成树的权值和
	connected = [[x] for x in vertexes]
	for edge in edges:
		# 如果边的两个顶点在最小生成树中都已经连接，就会形成环
		for i in range(len(connected)):
			if edge[0] in connected[i]:
				m = i				
		for i in range(len(connected)):
			if edge[1] in connected[i]:
				n = i
		if m != n:
			kruskal.append(edge)
			Sum += edge[2]
			connected[m] += connected[n]
			connected.remove(connected[n])

	return kruskal, Sum		
	

vertexes = ['A','B','C','D','E','F','G','H','I']
matrix = [[MAX,  10, MAX, MAX, MAX,  11, MAX, MAX, MAX],
		[10,  MAX,  18, MAX, MAX, MAX,  16, MAX,  12],
		[MAX,  18, MAX,  22, MAX, MAX, MAX, MAX,   8],
		[MAX, MAX,  22, MAX,  20, MAX, MAX,  16,  21],
		[MAX, MAX, MAX,  20, MAX,  26,   7,  19, MAX],
		[11,  MAX, MAX, MAX,  26, MAX,  17, MAX, MAX],
		[MAX,  16, MAX, MAX,   7,  17, MAX,  19, MAX],
		[MAX, MAX, MAX,  16,  19, MAX,  19, MAX, MAX],
		[MAX,  12,   8,  21, MAX, MAX, MAX, MAX, MAX]]
edges = []
for i in range(9):
	for j in range(i):
		if matrix[i][j] != MAX:
			edges.append([vertexes[j],vertexes[i],matrix[i][j]])

primtree = prim_tree(9, matrix)
print(primtree)
print(kruskal_tree(vertexes, edges))

# A——B权值：10
# A——F权值：11
# B——I权值：12
# I——C权值：8
# B——G权值：16
# G——E权值：7
# G——H权值：19
# H——D权值：16
# Sum=99
# 插入结点顺序：['A', 'B', 'F', 'I', 'C', 'G', 'E', 'H', 'D']


