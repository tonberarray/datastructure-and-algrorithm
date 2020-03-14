# 并集
A =[20,30,51,61]
B=[63,20,65,61]
m=len(B)
for i in range(m):
	if B[i] not in A:
		A.append(B[i])

A.insert(2,'hello')	
print(A)
A.remove(51)
print(A)
A.pop(1)
print(A)
A.pop()
print(A)			