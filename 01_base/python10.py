## 切片
## [start_index,end_index)左闭右开
## [start index,end index step]
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list[2:4])
print(list[1:7])
print(list[1:7:2])
print(list[3:2:1])

list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(list[1:5])
## 默认从0开始
print(list[:5])

print(list[:3:2])

print(list[:10000:1])

print(list[::1])
print(list[::2])
## 倒叙
print(list[::-1])
