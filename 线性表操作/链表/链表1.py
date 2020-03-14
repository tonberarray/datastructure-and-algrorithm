 # 链表实现


class IntNode(object):
	"""docstring for IntNode"""
	def __init__(self, i, n):
		self.item = i
		self.next = n


class SLList(object):
	"""docstring for SLList"""
	def __init__(self, x):
		self.__first = IntNode(x, None)
		self.__size = 1

	def add_first(self, x):
		self.__first = IntNode(x, self.__first)
		self.__size += 1

	def add_last(self, x):
		p = self.__first
		while p.next is not None:
			p = p.next	
		p.next = IntNode(x, None)
		self.__size += 1

	def get_first(self):
		return	self.__first.item

	def get_size(self):
		return self.__size

	def get(self, i):
		if i == 0:
			return self.__first.item
		else:
			return self.__first.get(i-1) 

						
l = SLList(10)
print(l.get_first())
l.add_first(15)
print(l.get_first())
l.add_first(19)
l._SLList__first.item = 8
# l.first.item = 8
l.add_last(9)
l.add_last(6)
print(l.get_first())
print(l.get_size())
print(f'size: {l.get_size()}')


# l1= SLList()

class Intlist(object):
	"""docstring for Intlist"""
	def __init__(self, f, r):
		self.first = f
		self.rest = r
		
	# def size(self):
		# if self.rest is None:
		# 	return 1
		# else:
		# 	return 1 + self.rest.size()
	
	def iterative_size(self):
		p = self
		total_size = 0
		while p is not None:
			total_size += 1
			p = p.rest
		return total_size	

	def get(self, i):
		if i == 0:
			return self.first
		else:
			return self.rest.get(i - 1)	
		

# l = Intlist(10, None)
# l = Intlist(14, l)
# l = Intlist(19, l)
# print(l.get(0))


