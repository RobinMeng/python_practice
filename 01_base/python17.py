## set 交叉并补 处理
a = set(range(50))
b = set(range(100))

## U 集
print(a.union(b))
## N 集
print(a.intersection(b))
## 差集
print(b.difference(a))
## a 是否时子集
print(a.issubset(b))
## b 是否时父集
print(b.issuperset(a))
