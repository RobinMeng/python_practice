## 装饰器，不改变代码现有情况，为函数添加功能，类似于切面
def log(f):
    ## 打包传惨
    def logging(*args, **kwargs):
        print("开始处理")
        ## 解包
        r = f(*args, **kwargs)
        print(f"当前处理结果 {r}")
        print("结束处理")
        return r

    return logging


@log
def add(a, b):
    return a + b


@log
def hello_world():
    print("hello world")

print(add(1, 2))

print(hello_world())
