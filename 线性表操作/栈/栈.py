# 堆栈的实现 元素后进先出
## binary to decimal
'''二进制转化为十进制时的公式：
a1*2^0 + a2*2^1 +a3*2^2+...+an*2^(n-1)
a1,a2...an二进制从低到高位的值
'''
## binary to octal
'''二进制转化为八进制时，二进制数每三个位对应八进制一个位数
即a1*2^0+a2*2^1+a3*2^2 对应oct第一位数，以此类推，得八进制数
a1,a2...an二进制从低到高位的值
'''

## binary to hexadecimal
'''二进制转化为十六进制时，二进制数每四个位对应十六进制一个位数
即a1*2^0+a2*2^1+a3*2^2+a4*2^3 对应hex第一位数，以此类推，得十六进制数
a1,a2...an二进制从低到高位的值
'''
## 单链表实现堆栈时，top指向链表的头部，底部bottom为None
## 链表头部操作实现入栈和出栈

# 顺序表（数组）实现堆栈
import sys


class Stack(object):
	"""docstring for Stack"""
	def __init__(self, size):
		self.stack = []
		self.maxsize = size
		self.top = -1
		self.maxval = -sys.maxsize - 1
		self.maxstack = []

	def push(self, x):
		"""入栈，先检测栈是否已满"""
		if self.isfull():
			raise Exception('stack is full')	
		else:
			if x > self.maxval:
				self.maxval = x
				self.maxstack.append(x)
			self.stack.append(x)
			self.top += 1

	def pop(self):
		"""出栈，先检测栈是否已空"""
		if self.isempty():
			raise Exception('stack is empty')
		 
		# 如果弹出的元素为当前堆栈的最大值，maxstack也要弹出栈顶元素
		if self.peek() == self.maxval:
			self.maxstack.pop()
			self.maxval = self.maxstack[len(self.maxstack)-1]
		self.top -= 1
		return self.stack.pop()

	def peek(self):
		"""查看栈顶的元素，不弹出"""
		if self.isempty():
			raise Exception('stack is empty')
		else:
			return self.stack[self.top]

	def isempty(self):
		return self.stack == []

	def isfull(self):
		return self.top + 1	== self.maxsize

	def length(self):
		return len(self.stack)	

	def max(self):
		"""当前栈中最大值"""
		return self.maxval	

l = Stack(10)
print(l.pop())
