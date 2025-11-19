## 向外抛异常

def div_num(a, b):
    if not isinstance(a, int):
        raise TypeError('参数类型错误')
    if not isinstance(b, int):
        raise TypeError('参数类型错误')
    if 0 == b:
        raise ZeroDivisionError('除数为0')
    val = a / b
    print(val)


try:
    div_num('hello', 1)
except BaseException as e:
    print(e)

try:
    div_num(1, 'hello')
except BaseException as e:
    print(e)
try:
    div_num(1, 0)
except BaseException as e:
    print(e)
