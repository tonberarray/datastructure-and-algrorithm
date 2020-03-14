# 归并排序


def mergesort(datas):
	if len(datas) <=1:
		return datas

	half = len(datas)//2
	first = mergesort(datas[0:half])
	second = mergesort(datas[half:len(datas)])
	i = 0
	j = 0
	new = []
	while  i < len(first) or j < len(second):
		if i < len(first) and j < len(second):
			if first[i] < second[j]:
				new.append(first[i])
				i += 1 
			else:
				new.append(second[j])
				j += 1	
			
		else:
			if i < len(first):
				new.append(first[i])
				i += 1
			if j < len(second):
				new.append(second[j])			
				j += 1	

	return new

datas = [6,4,9,2,5,7,10,1,3,8]
print(mergesort(datas))	
