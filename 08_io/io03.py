import os

## 写数据
lines = ['今天', '测试', '.']
with open('./data02.txt', mode='w', encoding='utf-8') as f:
    f.write("hello world\n")
    f.writelines(lines)

## 读取写入文本数据
with open('./data02.txt', encoding='utf-8') as f2:
    print(f2.read())

## 文件分割符
print(os.sep)
