# for
for item in range(100):
    print(item)

_list = ['a', 'b', 'c']
_list2 = [5, 6, 7]
for item in _list:
    print(item)

## 加上循环计数器
for idx, v in enumerate(_list):
    print(idx, '--------', v)
## 同时循环两个变量
## zip() 就是**“把多个列表按位置拉到一起”**的最简洁工具。
for a, b in zip(_list, _list2):
    print(a, '----', b)

## 反向循环
## reversed()
for item in reversed(range(5)):
    print(item)

for item in reversed(_list):
    print(item)
