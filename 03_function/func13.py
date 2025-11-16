# 完整函数

def func(a: int, b: str, c: bool) -> str:
    print(a)
    print(b)
    print(c)
    return '123'


## 参数注释
def func02(a: 'str字符串', b: 'bool值', c: 'number 值') -> '返回字符串':
    print(a, b, c)
    return 'hello world'


print(func(1, '2', False))

print(func02(1, 2, 3))
