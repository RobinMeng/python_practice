## 可变参数
## 打包传惨
def add(a, b, *args):
    print(f"第一个参数:{a}")
    print(f"第二个参数:{b}")
    print(args)
    return a + b


print(add(1, 2, 3, 4, 5, 5, 6))


##可变长字典参数
def add2(a, b, **kwargs) -> None:
    print(kwargs)


print(add2(1, 2, c=2, d=4))
