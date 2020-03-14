# knapsack problem
# 动态规划求解背包问题
import numpy as np

def main():	
	w = [1, 4, 3] # 物品对应的重量
	val = [1500, 3000, 2000] #物品对应的价值
	M = 4 # 背包的容量
	n = len(val) # 物品的个数
	# 创建二维数组
	# v[i][j] 表示在前i个物品中能够装入容量为j的背包中的最大价值
	v = np.zeros((n+1, M+1))
	path = np.zeros((n+1, M+1))	# 记录背包装入的物品
	# 初始化二维数组的第一行和第一列为零
	for i in range(1,n+1):
		for j in range(1,M+1):
			if w[i-1] > j:
				v[i][j] = v[i-1][j]
			elif val[i-1] + v[i-1][j-w[i-1]] > v[i-1][j]:
				v[i][j] = val[i-1] + v[i-1][j-w[i-1]]
				path[i][j] = 1
			else:
				v[i][j] = v[i-1][j]	

	print(v)
	print(path)
	# 输出我们放入了那些物品
	# 我们只需要输出最终放入的物品	
	for i in range(n,0,-1):
		if path[i][M] == 1:
			print("第%d个物品放入背包"%i)
			M -= w[i-1]


if __name__ == '__main__':
	main()					
	# array = np.zeros((4,5))
	# print(array)
