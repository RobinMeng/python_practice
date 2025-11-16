## 返回多个值

def calc(a=1, b=1):
    return a + b, a - b


print(calc(2, 3))

(c, d) = calc(3, 4)
print(c)
print(d)
