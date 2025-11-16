## 列表推导式
##新列表元素 for 元素 in 列表
## 新列表元素 for 元素 in 列表 if条件
_list = [1, 2, 3]

_list1 = [val * 2 for val in _list]
print(_list1)

_list2 = [val * 3 for val in _list]
print(_list2)

_list3 = [var * 4 for var in _list if var % 2 == 0]
print(_list3)
