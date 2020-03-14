# coding=utf-8
S = [10,4,8,7,9,6,2,5,3]
minPrice = S[0]
N = 0 
profit = 0
selday = 0 
buyday = 0
for N in range(len(S)):
	if (S[N]<minPrice):
		minPrice = S[N]
		buyday=N

	if (S[N]-minPrice>profit):
		profit = S[N]-minPrice
		selday=N

print("在第{0}天买入，第{1}天卖出，最大收益：{2}".format
	(buyday+1,selday+1,profit))

S = [10,4,8,7,9,6,2,5,3]
maxprofit = 0
buyDay=0
selDay=0

for i in range(len(S)-1):
	for x in range(i+1,len(S)):
		if S[x]-S[i]>maxprofit:
			maxprofit=S[x]-S[i]
			buyDay=i
			selDay=x

print("在第{0}天买入，第{1}天卖出，最大收益：{2}".format
	(buyDay+1,selDay+1,maxprofit))
		