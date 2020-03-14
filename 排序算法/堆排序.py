# 堆排序，完全二叉树，大顶堆，小顶堆，层序遍历
"""大顶堆：完全二叉树中，每个节点的值都大于等于其左右子节点的值，根节点为最大"""
"""小顶堆：完全二叉树中，每个节点的值都小于等于其左右子节点的值，根节点为最小"""

def maxheap(datas, i, n):
	
	left = 2*i+1
	right = 2*i+2
	MAX = i
	if left < n and datas[left] > datas[MAX]:
		MAX = left
	if right < n and datas[right] > datas[MAX]:
		MAX = right

	if MAX != i:
		temp = datas[i]
		datas[i] = datas[MAX] 
		datas[MAX] = temp
		maxheap(datas,MAX,n)

def heapsort(datas):
	n = len(datas)
	i = n//2
	while i >= 0:
		maxheap(datas, i, n)
		i -= 1

	j = n-1	
	while j > 0:
		temp = datas[0]
		datas[0] = datas[j]	
		datas[j] = temp
		maxheap(datas,0, j)
		j -= 1
	return datas

datas = [6,4,9,2,5,7,10,1,3,8]	
print(heapsort(datas))


class HeapSort(object):
	"""docstring for Heapsort"""
	def __init__(self, array):
		self.heapsize = len(array)
		self.array = array

	def parent(self, i):
		return i//2
		
	def left(self, i):
		return 2*i

	def right(self, i):
		return 2*i+1	

	def maxHeapify(self, i):
		"""把下标为i的节点与子节点互换，先找出左右子节点最大值，
		然后将前当节点与其互换，进入换过的节点，继续进行置换流程
		直到底部，从而维持堆的性质"""
		# 把下标i+1，因为数组下标从0开始， 但是算法从元素下标从1开始			
		i += 1
		left = self.left(i)
		right = self.right(i)
		# 把下标i-1，因为数组下标从0开始， 但是算法从元素下标从1开始	
		i -= 1
		left -= 1
		right -= 1
		# 从左右孩子节点中找出最大的那个
		Max = i
		if left < self.heapsize and self.array[left] > self.array[i]:
			Max = left

		if right < self.heapsize and self.array[right] > self.array[Max]:
			Max = right	

		if Max != i:
			temp = self.array[i]
			self.array[i] = self.array[Max]
			self.array[Max] = temp
			self.maxHeapify(Max)
 
	def buildMaxheap(self):
		i = self.heapsize//2
		while i >=0:
			self.maxHeapify(i)
			i -= 1
		return self.array
		

array = [6,4,9,2,5,7,10,1,3,8]
hs = HeapSort(array)
heap = hs.buildMaxheap()
print(heap)
