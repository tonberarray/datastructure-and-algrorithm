# 动态规划
"""给定一根单位长度的钢管，
切出不同的长度卖出不同的价钱，
要求设计一个有效算法，使得切出来的钢管卖出最高的价钱"""

import sys


class BestCut(object):
	"""docstring for BestCut"""
	# 记录给定长度的最优切割方案，
	# length对应长度，price对应最优价格，cuts对应切割方式
	def __init__(self, length, price, cuts):
		self.rodlength = length
		self.bestPrice = price
		self.bestcuts = cuts

	def printcut(self):
		print('length:{0},price:{1}'.format(self.rodlength, self.bestPrice))	


def recursiveCutRod(priceTable, length, bestCutMap):
	if bestCutMap.get(length):
		#当前给定长度的最优切割方案已经找到
		return bestCutMap[length]
	q = None 
	if length <= 0:
		q = BestCut(0, 0, None)
	elif length == 1:
		#单位长度不能继续往下切割
		return BestCut(1, priceTable[1], None)
	else:
		currentPrice = -sys.maxsize
		bestCut1 = None 
		bestCut2 = None
		for i in range(1, length):
			#把长度为length的钢管切割成i和length - i，然后递归的查找两部分的最优切割方案
			cut1 = recursiveCutRod(priceTable, i, bestCutMap)
			cut2 = recursiveCutRod(priceTable, length - i, bestCutMap)
			if cut1.bestPrice + cut2.bestPrice > currentPrice:
				currentPrice = cut1.bestPrice + cut2.bestPrice
				bestCut1 = cut1
				bestCut2 = cut2 
		#如果长度在价格表内，看看整体出售是不是更好
		if length < len(priceTable) and priceTable[length] > currentPrice:
			bestCutMap[length] = BestCut(length, priceTable[length], None)
			return bestCutMap[length]
		
		bestCutArray = [bestCut1, bestCut2]
		bestCutMap[length] = BestCut(length, currentPrice, bestCutArray)
		#积累
		return bestCutMap[length]
			


def cutrod(pricetable, length):
	"""钢管切割参数传递"""
	bestCutMap = {}
	return recursiveCutRod(pricetable, length, bestCutMap)


def getbestcuts(cut, cutlist):
	"""找出最优方案"""
	#当BestCut的bestcuts为空时，他本身即是最优切割的一部分		
	if cut.bestcuts is None:
		cutlist.append(cut)
		return
	else:
		for subcut in cut.bestcuts:
			getbestcuts(subcut, cutlist)	


pricetable = [0,1,5,8,9,10,17,18,20,24,30]
length = 15
cut = cutrod(pricetable, length)
cutlist = []
getbestcuts(cut, cutlist)
print(f"the bestprice for rod with length {length} is {cut.bestPrice}")
print(f"The best way to cut the rod with length of {length} are:")
for cut in cutlist:
	cut.printcut() 
	