## 字典推到式

a = {"1": "test", "2": "hello", "3": "world"}

print(a)

b = {val + '...' for k, val in a.items()}

print(b)

c = {k: val + '...' for k, val in a.items()}
print(c)

d = [val + '<><><>' for k, val in a.items()]

print(d)
