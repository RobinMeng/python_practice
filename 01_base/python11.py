## 更新列表

list = [1, 2, 3, 4, 5, 7, 8, 9, 0]

print(list[0])
list[0] = -1
print(list[0])

## 嵌套列表
list = [1, 2, 3, 4, [1, 2, 3, 4]]

print(list)
print(list[-1][2])
## 列表元素
print(len(list))

## 列表添加 和 插入
list.append(9)
print(list)
list.insert(0, 9)
print(list)

## 列表元素删除

del list[0]
del list[-1]
print(list)

list.remove(2)
print(list)

print(list.pop(0))
print(list)

print(list.pop(-1))

## 搜索
print(list)
print(list.index(3))
