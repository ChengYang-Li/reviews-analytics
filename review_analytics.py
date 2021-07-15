# 留言分析程式

datas = []
count = 0
length = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		datas.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(datas))

for data in datas:
	length += len(data)


print('檔案讀取完了，總共有', len(datas), '筆資料喔~')
print('每筆留言的平均長度為', length / len(datas))
