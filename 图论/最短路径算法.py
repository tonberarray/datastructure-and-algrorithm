# 最短路径算法
# Dijkstra算法
# Floyd算法,
MAX = float('inf')

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


def dijkstra(vertexes, matrix): 
	"""邻接矩阵，求v[0]到v[w]的最短路径"""
	num = len(vertexes) 
	minweight = [0]
	final = [False]*num
	# path[k]保存的值为与下标为k的顶点距离最近(权值最小)的顶点
	# 数组在这里的用途有点类似于KMP算法中的next数组
	path = [vertexes[0]] 
	final[0] = True
	for i in range(1,num):
		path.append(vertexes[0])
		minweight.append(matrix[0][i])
	for _ in range(1,num):
		Min = MAX
		k = 0
		for x in range(num):
			if (not final[x]) and minweight[x] < Min:
				k = x
				Min = minweight[x]
		final[k] = True
			
		for j in range(num):
			if (not final[j]) and matrix[k][j] + Min < minweight[j]:
				minweight[j] = matrix[k][j] + Min
				path[j] = vertexes[k]
				
	return path, minweight


def floyd(vertexes,matrix):
	"""邻接矩阵，求图中任意顶点到另一顶点的最短路径"""
	minweight = matrix
	num = len(vertexes)
	path = [[x for x in range(num)]for x in range(num)]

	for k in range(num):
		for i in range(num):
			for j in range(num):
				if minweight[i][j] > minweight[i][k] + minweight[k][j]:
					minweight[i][j] = minweight[i][k] + minweight[k][j]
					path[i][j] = path[i][k]
	return path, minweight



  

print(dijkstra(vertexes,matrix)) 
path, minweight = floyd(vertexes,matrix)
for x in path:
	print(x)
print('*'*25)
for y in minweight:
	print(y)	
