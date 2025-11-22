import os

## 获取当前路径下的文件
print(os.listdir())

## 判断是否是路径
print(os.path.isdir("./datas"))
print(os.path.isdir("../08_io"))

## 判断是否是文件
print(os.path.isfile("./datas"))
print(os.path.isfile("./data.txt"))

## 获取扩展名称

path = os.getcwd()

print(os.path.splitext(path))

print(os.path.splitext('./data.txt'))
