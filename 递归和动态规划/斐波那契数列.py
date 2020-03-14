# 斐波那契数列fibonacci sequence，递归recursion,黄金分割
"""
典型的斐波那契递归问题
青蛙跳级问题：一只青蛙上台阶，一次可以跳一级台阶或者两级台阶，
有n级的台阶，试问青蛙有多少种跳上去的方法。
"""

def fib(n):
	"""递归"""
	if isinstance(n, int) == False or n < 0:
		raise RuntimeError('invalid parameter')

	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		 return fib(n-1) + fib(n-2)

	
def fibonacci(n):
	"""迭代"""
	if isinstance(n, int) == False or n < 0:
		raise RuntimeError('invalid parameter')
	m, a, b = 0, 0, 1
	while m < n: 
		print(b, end=' ')
		a, b = b, a + b
		m += 1
	print('')


def create_fib_sequence(n):
	if isinstance(n, int) == False or n < 0:
		raise RuntimeError('invalid parameter')
	sequence = [0]*(n+1)
	if n > 0:
		sequence[1] = 1
	if n > 1:
		for i in range(2,n+1):
			sequence[i] = sequence[i-1] + sequence[i-2]
	return sequence		
	

fibonacci(21)
print(fib(21))
sequence = create_fib_sequence(21)
print(sequence)
print(sequence[20]/sequence[21])

