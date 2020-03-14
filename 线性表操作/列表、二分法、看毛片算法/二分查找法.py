# -*- coding: utf-8 -*-
# 升序 递归,分而治之（二分法）
def binaryFind(A, m):
	if len(A) == 0:
		return -1

	i = int(len(A) / 2)
	if A[i] == m:
		return i
	if A[i] > m and i - 1 >= 0:
		return binaryFind(A[0:i - 1], m)
	if A[i] < m and i + 1 < len(A):
		return binaryFind(A[i:len(A)], m)

	return -1


A = [3, 1, 5, 6, 7, 4, 2, 8]
A.sort()
M = 9
success = False
for i in range(len(A)):
	m = M - A[i]
	j = binaryFind(A, m)
	if j != -1 and j != i:
		print("存在i和j使得A[i]+A[j]= {0}".format(M))
		success = True
		break
if success != True:
	print("不存在i和j使得A[i]+A[j]= {0}".format(M))



def binary_search(the_array, item, start, end):#二分法插入排序
	if start > end:
		return 
 
	mid = round((start + end)/ 2)
 
	if the_array[mid] < item:
		return binary_search(the_array, item, mid + 1, end)
 
	elif the_array[mid] > item:
		return binary_search(the_array, item, start, mid - 1)
 
	elif the_array[mid] == item:
		return mid
	return None    


def binary_find(datas):
		pass	