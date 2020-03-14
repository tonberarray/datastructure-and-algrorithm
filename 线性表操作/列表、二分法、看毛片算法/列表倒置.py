# reverse 
def reverse(datas):
	if len(datas) <2:
		return datas
	l = len(datas)	
	i = 0
	while i < (l - 1)/2:
		datas[i], datas[l - i -1] = datas[l - i -1], datas[i]
		i += 1
	return datas	

datas =[x for x in range(11)]	
print(datas)
reverse(datas)
print(datas)
