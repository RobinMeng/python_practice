## ()元组 不可变列表
_tuple = (1, 2, 3, 4, 5)

print(_tuple)

print(_tuple.count(2))
print(_tuple.index(1))

_list = [2, 4, 6, 8, 10]
print(_list)
a = tuple(_list)
print(a)
print(a[0:])
print(a[0:-1])
print(a[0::2])
print(len(a))
