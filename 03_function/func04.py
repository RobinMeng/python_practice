# 使用默认参数

def add(a=1, b=2, c=3):
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")
    return a + b + c


print(add())
print(add(2))

print(add(2, 3))
print(add(c=4))
