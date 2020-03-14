# 八皇后问题，递归实现
"""在8×8的国际象棋棋盘上，摆放八个皇后，
并且每一行每一列每一斜线方向只能有一个皇后，
保证皇后不能相互攻击，总共有多少种摆法"""
# def drop_place(pos,status):
# 	nextY = len(status) 
# 	for i in range( nextY ): 
# 		if abs(status[i] - pos ) in (0, nextY - i ):
# 			return True 
# 	return False 

# def queens(num=8, status=[] ):
# 	for pos in range(num):
# 		if not drop_place(pos,status):
# 			if len(status) == num - 1:
# 				yield [pos,]
# 			else:
# 				for result in queens(num, status +[pos,]):
# 					yield [pos,]+result

# for n in queens(8):
# 	print(n)


def notattack(chess, row, col):
	for x in range(row):
		if abs(chess[x]-col) in (0, row-x):
			return False
	return True		


count = 0
def eightqueens(chess, row=0):
	global count
	if row ==len(chess):
		print(count +1, chess)
		count += 1
		return 
	for col in range(len(chess)):
		if notattack(chess, row, col):
			chess[row] = col	
			eightqueens(chess, row+1)


chess = [0]*8
eightqueens(chess)
