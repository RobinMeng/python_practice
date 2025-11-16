## yield next

def say():
    print("开始")
    yield "hello"
    print("继续1")
    yield "world"
    print("继续2")
    yield "你好"


print(next(say()))
print(next(say()))
print(next(say()))

func = say()

print(next(func))
print(next(func))
print(next(func))
