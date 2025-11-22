## 获取当前路径

import os

## cmd 获得绝对路径
path = os.getcwd()
print(path)

## 绝对路径
print(os.path.abspath(path))

## 检查路径是否存在

print(os.path.exists(path))
print(os.path.exists('c:/text.txt'))
