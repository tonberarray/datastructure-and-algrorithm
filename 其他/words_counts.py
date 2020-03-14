# 词频统计

def find_word_count(words):
	words_count = {}  # dict字典
	for word in words:
		if word in words_count:
			words_count[word] += 1
		else:	
			words_count[word]=1

	return words_count		


words =[]	# 列表
file_name='my_dream.txt'
with open(file_name, 'r') as f:
	lines= f.readlines()
	for line in lines:
		line = line.replace(',', ' ')
		line = line.replace('.', ' ')
		line = line.replace('"', ' ')
		line = line.replace('-', ' ')
		line = line.replace('\n', ' ')
		line = line.replace('?', ' ')
		line = line.replace('!', ' ')
		line = line.replace('\'', ' ')
		line = line.replace(':', ' ')

		for word in line.split(' '):
			if word:
				words.append(word)

print(len(words))
words_set =set(words) # 集合
print(len(words_set))
print(find_word_count(words))				