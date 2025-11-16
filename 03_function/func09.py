# nonlocal

def add(a, b, c):
    count = a + b + c

    def sub_add():
        ## 修改嵌套作用域的变量，nonlocal 不上全局，不下局部，只盯外层函数
        nonlocal count
        count += 1
        return count

    sub_add()
    sub_add()
    return count


print(add(1, 2, 3))
