## set
a = {1, 3, 5, 7}
print(a)

b = {1, 3, 5, 7, 7}

print(b)

c = set(range(100))
print(c)
d = set(list(range(100)))
print(d)

d.add(101)
print(d)
d.remove(101)
print(d)
print(1 in d)
print(1000 in d)

## 全部删除
d.clear()
print(d)
