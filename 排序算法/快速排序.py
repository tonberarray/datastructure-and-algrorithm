# 快速排序


def quicksort(datas):
	if len(datas) < 2:
		return datas
	pivot = datas[len(datas)//2]
	datas.remove(pivot)
	left = [val for val in datas if val < pivot]
	right = [val for val in datas if val >= pivot]
	return quicksort(left) + [pivot] + quicksort(right)	


datas = [6,4,9,2,5,7,10,1,3,8]
print(quicksort(datas))	