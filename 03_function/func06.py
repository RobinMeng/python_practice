# 引用外部变量
a = 10


def func():
    print(a)


func()


## 更新外部变量
def func02():
    global a
    a += 1
    print(a)


func02()

print('----->', a)
