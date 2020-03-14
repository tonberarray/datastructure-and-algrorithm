# 动态规划 查找最大共同子串 比较字符串的相似程度

UP = 0
LEFT = 1
UP_LEFT = 2
# 数组C用于记录最大共同子串长度，
#C[i][j]记录长度为i的X序列和长度为j的Y序列的最大共同子串
# B 用于记录相关信息，构造最大共同子串
C = []
B = []

def getlongcommonstringlength(X, Y):
	m = len(X)
	n = len(Y)
	for i in range(m+1):
		C.append([])
		B.append([])
		for j in range(n+1):
			C[i].append(0)
			B[i].append(UP)
	for i in range(1,m+1):
		for j in range(1,n+1):
			if X[i-1]==Y[j-1]:
				C[i][j] = C[i-1][j-1] + 1
				B[i][j] = UP_LEFT
			elif C[i-1][j] >= C[i][j-1]:
				C[i][j]	= C[i-1][j] 
				B[i][j] = UP
			else:
				C[i][j] = C[i][j-1]
				B[i][j] = LEFT


def getlongcommonstring(X, Y, i, j):
	if i == 0 or j == 0:
		return ''
	lcs = ''
	if B[i][j] == UP_LEFT:
		lcs = getlongcommonstring(X, Y, i-1, j-1)
		lcs += X[i-1]
	elif B[i][j] == UP:	
		lcs = getlongcommonstring(X, Y, i-1, j)	
	else:
		lcs = getlongcommonstring(X, Y, i, j-1)	
	return lcs


X = 'ABCBDAB'
Y = 'BDCABA'	
getlongcommonstringlength(X, Y)
lcs =getlongcommonstring(X, Y, len(X), len(Y))
print(lcs)
for i in C:
	print(i)
print('*'*25)
for j in B:
	print(j)

"""
X = 'ABCBDAB'
Y = 'BDCABA'	
BCBA
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 1, 1]
[0, 1, 1, 1, 1, 2, 2]
[0, 1, 1, 2, 2, 2, 2]
[0, 1, 1, 2, 2, 3, 3]
[0, 1, 2, 2, 2, 3, 3]
[0, 1, 2, 2, 3, 3, 4]
[0, 1, 2, 2, 3, 4, 4]
*************************
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 2, 1, 2]
[0, 2, 1, 1, 0, 2, 1]
[0, 0, 0, 2, 1, 0, 0]
[0, 2, 0, 0, 0, 2, 1]
[0, 0, 2, 0, 0, 0, 0]
[0, 0, 0, 0, 2, 0, 2]
[0, 2, 0, 0, 0, 2, 0]
"""


def modifiedgetlongestcommontsubstringlength(X, Y):
	m = len(X)
	n = len(Y)

	A = [[], []]
	for j in range(n+1):
		A[1].append(0)

	for i in range(1,m+1):
		A[0] = []
		for j in range(len(A[1])):
			A[0].append(A[1][j])

		for j in range(1,n+1):	
			if X[i-1]==Y[j-1]:
				A[1][j] = A[0][j-1] + 1
			elif A[0][j] >= A[1][j-1]:
				A[1][j]	= A[0][j] 
			else:
				A[1][j] = A[1][j-1]

	return A[1]


def getlongestcommonsubstringwithlinearspace(X, Y):
	if len(Y) == 0:
		return ''
	if len(X) == 1:
		for j in range(len(Y)):
			if X[0]	== Y[j]:
				return X[0]
		return ''
	m = len(X)	
	n = len(Y)
	i = m // 2	
	L1 = modifiedgetlongestcommontsubstringlength(X[0:i], Y)
	X1 = X[::-1]	
	Y1 = Y[::-1]
	L2 = modifiedgetlongestcommontsubstringlength(X1[0:m-i],Y1)

	L = 0
	k = 0
	for j in range(n+1):
		if L1[j] + L2[n-j] > L:
			L = L1[j] + L2[n-j]  
			k = j

	S1 = getlongestcommonsubstringwithlinearspace(X[0:i],Y[0:k])
	S2 = getlongestcommonsubstringwithlinearspace(X[i:m],Y[k:n])

	return S1 + S2

X = 'ABCBDAB'
Y = 'BDCABA'

L = getlongestcommonsubstringwithlinearspace(X, Y)
print(f"The longest sub string of {X} and {Y} is {L}")
"""The longest sub string of ABCBDAB and BDCABA is BDAB"""