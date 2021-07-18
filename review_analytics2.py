# 留言分析程式


# 讀取檔案
def read_file(filename):
	datas = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			datas.append(line.strip())
	return datas


# 統計字數
def word_count(datas):
	#words_list = []
	words = {}
	for data in datas:
		#data = data.split(' ')
		data = data.split() # split的預設就是空白而且用預設的方式寫可以避免連續空白切出空字串
		for d in data:
			#if d in words_list: #list跟dict速度差異非常大
			if d in words:
				# count = words[d] # 查這個字目前的count 
				# count += 1 # count加一
				# words[d] = count # 更新字典
				words[d] += 1
			else:
				#words_list.append(d) # 把新字加進清單
				words[d] = 1 # 在字典中建立新字且計數1
	for w in words:
		if words[w] > 1000000:
			print('超過一百萬的字', w, words[w])
	print('總共有', len(words), '字可以查')
	return words


#查詢字
def select(words):
	while True:
		word = input('請輸入要查詢的字，按q離開: ')
		if word == 'q':
			break
		elif word not in words:
			print('查無此字，請重新輸入')
			continue
		print('你查詢的字', word, '總共出現', words[word], '次')


# main
def main():
	datas = read_file('reviews.txt')
	words = word_count(datas)
	select(words)


if __name__ == '__main__':
	main()