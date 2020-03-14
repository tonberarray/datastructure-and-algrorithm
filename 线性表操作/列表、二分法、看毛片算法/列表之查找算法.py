# 数组查找方案
"""数组查找，先对数值进行排序处理，然后进行查找搜索"""
def find1(datas, key):
	if len(datas) == 0:
		return None
	m = len(datas)
	for x in range(m):
		if datas[x] == key:
			return x
	return None


def find2(datas, key):
	if len(datas) == 0:
		return None
	m = len(datas) - 1
	datas[0] = key
	while datas[m] != key:
		m -= 1
	return m


def binaryfind(datas, key):
	start = 0
	end = len(datas) - 1
	if start > end:
		return None

	while start <= end:
		i = (end - start) // 2 + start
		if datas[i] == key:
			return i
		elif datas[i] >	key:
			end = i - 1
			continue
		else:
			start = i + 1
			continue
	return None		
		

def binaryfind2(datas, key):
	"""按比例折半查找，该方法只适合均匀分布的数值查找"""
	if len(datas) == 0:
		return None
	i = int((key - datas[0])/(datas[-1] - datas[0]) * len(datas))
	
	if datas[i] == key:
		return i
	
	if datas[i] > key:
		return binaryfind2(datas[0:i-1],key) 
	if datas[i]	< key:
		return binaryfind2(datas[i:len(datas)],key)

	return None	


datas = [x for x in range(26)]
# datas.sort()
print(binaryfind(datas, 14))
# key = 'M'
