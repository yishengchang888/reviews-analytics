data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))


sum_len = 0
for _ in data:
    sum_len += len(_)
    print(sum_len)
print('檔案讀取完了，總共有 ', len(data), ' 筆資料')
print('留言的平均長度為： ', sum_len / len(data))

new = []
for _ in data:
    if len(_) < 100:
        new.append(_)

print('一共有 ', len(new), '筆留言長度小於100')
print(new[0])


good = []
for _ in data:
    if 'good' in _:
        good.append(_)

print('一共有', len(good))
print(good[0])

