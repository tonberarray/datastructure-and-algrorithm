# 堆栈,逆波兰表达式（运算符后缀表达式）Notation
"""逆波兰表达式：Reverse Polish Expression
计算机进行数学运算时，要先对算法的优先级进行条件判断
如果计算机接收的运算输入方式是传统的输入，
如{[(1-2)*(4+5)+1]+[(1-2)*(4+5)-9]}*8+14
计算机进行的条件判断将极为复杂的，【divisor(除数)】
为便于计算机的读取运算，计算机的运算输入采用运算符后缀表达式，
以堆栈的方式进行操作
a+b ---> a,b,+
a+(c-b)---> a,c,b-,+"""
# 表达式以字符串形式输入,逗号分隔字符 如'3,4,*,1,2,+,+'


class ReversePolishExpr(object):
	def __init__(self, expr):
		self.stack = []
		self.expression = expr

	def calculation(self):
		"""对后缀表达式字符串进行运算处理"""
		exprs = self.expression.split(',')		
		for expr in exprs:
			# 如果当前字符是运算符，并且入栈少于两个元素，则不能运算
			if self.isOperator(expr) and len(self.stack) < 2:
				raise RuntimeError('stack less then 2 elements')
			# 如果当前字符是运算符，弹出栈顶两个元素进行计算，计算结果入栈
			if self.isOperator(expr):
				self.docalculation(expr)
			else:
			# 如果当前字符是数字，将其转换成整数后入栈
				self.stack.append(int(expr))

		return  self.stack.pop()

	def isOperator(self, expr):
		"""判断是否为运算符"""
		if expr == "+" or expr == "-" \
		or expr == "*" or expr == "/":
			return True
		return False

	def docalculation(self, operator):
		# 如果当前字符是运算符，弹出栈顶两个元素进行计算，计算结果入栈
		n2 = self.stack.pop()
		n1 = self.stack.pop()

		if operator == "+":
			self.stack.append(n1 + n2)
		if operator == "-":
			self.stack.append(n1 - n2)
		if operator == "*":
			self.stack.append(n1 * n2)
		if operator == "/":
			if n2 == 0:
				raise RuntimeError('divisor is zero')
			self.stack.append(n1 / n2)

rp = ReversePolishExpr("3,4,*,1,2,+,+")	
print("result of reverse polish expression is {0}".format(rp.calculation()))		


# 中缀表达式转后缀表达式

# 中缀表达式转后缀表达式的规则：

# 1.遇到操作数，直接输出； 
# 2.栈为空时，遇到运算符，入栈； 
# 3.遇到左括号，将其入栈； 
# 4.遇到右括号，执行出栈操作，并将出栈的元素输出，直到弹出栈的是左括号，左括号不输出； 
# 5.遇到其他运算符’+”-”*”/’时，弹出所有优先级大于或等于该运算符的栈顶元素，然后将该运算符入栈； 
# 6.最终将栈中的元素依次出栈，输出。 
# 经过上面的步骤，得到的输出既是转换得到的后缀表达式。 

	 