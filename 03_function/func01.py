## 函数

## 有参数
def add(x, y):
    return x + y


## 无参数
def hello_world():
    print("hello world")


## 位置参数
def cube(x=1, y=1, z=1):
    print('x---->', x)
    print('y---->', y)
    print('z---->', z)
    return x * y * z


print(add(1, 2))
hello_world()
## 位置参数
print(cube(x=2, z=2))
