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

new = []

for data in datas:
	if len(data) <100:
		new.append(data)
print('留言小於100字的清單筆數總共有', len(new), '筆')

new_good = []

for data in datas:
	if 'good' in data:
		new_good.append(data)
print('留言裡有good的清單筆數總共有', len(new_good), '筆')
print(new_good[0])