## lambda 一种函数简写的方式，用于定义简单的函数
## 语法 lambda param:result
def add(a, b):
    return a + b


print(add(1, 3))

func = lambda a, b: a + b

print(func(1, 3))

func2 = lambda a, b, c: a + b + c

print(func2(1, 5, 5))
