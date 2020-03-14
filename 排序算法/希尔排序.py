# 希尔排序

def shellsort(datas):
	n = len(datas)
	if n < 2:
		return datas
	gap = n
	while gap > 1:
		gap = gap//3 + 1
		for i in range(gap, n):
			j = i
			while datas[j - gap] > datas[j] and j - gap >= 0:
				temp = datas[j]
				datas[j] = datas[j - gap]
				datas[j - gap] = temp
				j -= gap
	return datas			
				

datas = [6,4,9,2,5,7,10,1,3,8]
print(shellsort(datas))	