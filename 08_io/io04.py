## 合并路径
import os

file_path = os.path.join('.', 'data01.txt')

print(file_path)
## str 类型
print(type(file_path))

## 获取末尾及末尾以外的元组
path_split = os.path.split(file_path)
print(path_split)
print(type(path_split))

head, tail = os.path.split(file_path)

print(head)
print(tail)
