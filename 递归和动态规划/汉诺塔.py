# 汉诺塔，递归
i=1


def hano(n,A="A",B="B",C="C"):	
	global i
	if n == 1:
		print(f"第{i}步：移动{A}->{C}")
		i += 1
	else:
		hano(n-1,A,C,B)
		hano(1,A,B,C)
		hano(n-1,B,A,C)
hano(5)			