# KMP匹配 next数组
import time


def bruteforse(pattern, string):
	"""字符串暴力匹配"""
	i = j = 0 
	while i < len(string) and j < len(pattern):
		if string[i] == pattern[j]:
			i += 1
			j += 1
		else:
			i = i - j + 1
			j = 0
	if j == len(pattern):
		start = i - len(pattern)
		end = i -1	
		print((start,end))
	return None	



def getnext(pattern):
	nxt = [-1] * len(pattern)
	nxt[1] = 0
	i, j = 1, 0
	while i < len(pattern) - 1:
		if j == -1 or pattern[i] == pattern[j]:
			j += 1
			i += 1
			if pattern[i] == pattern[j]:
				nxt[i] = nxt[j]
			else:	
				nxt[i] = j
		else:		
			j = nxt[j]	
	return nxt


def kmp_match(pattern, string, pos=0):
	nxt = getnext(pattern)
	i = pos
	j = 0
	while i < len(string) and j < len(pattern):
		if j == -1 or string[i] == pattern[j]:
			i += 1
			j += 1
		else:
			j = nxt[j]
	if j == len(pattern):
		start = i - len(pattern)
		end = i -1	
		print((start,end))
	return None	 
 
# 测试
string = 'aabbaaaaaaaaaaaaaaaaaghgjhguygugjhhjghhbaaabacabaaba'
pattern = 'aabaca'
print(getnext(pattern))
t1 = time.perf_counter()
kmp_match(pattern,string)
t2 = time.perf_counter()
print('1所花时间：%s.5f ' %(t1-t2))
t3 = time.perf_counter()
bruteforse(pattern,string)
t4 = time.perf_counter()
print('2所花时间：%s.5f ' %(t1-t2))