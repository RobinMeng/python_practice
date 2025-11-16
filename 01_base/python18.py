## 字典 K_V
a = {"1": "test", "2": "hello"}
##### read
print(a)
## 取值
print(a["1"])
## 取值
print(a.get("1"))
## 取值并付默认值
print(a.get("100", "world"))

## write
a["1"] = "test1"
print(a)
print(a["1"])
a["5"] = "test5"

print(a)
print(list(a.keys()))
print(list(a.values()))

print(a.items())

for k, v in a.items():
    print(k, "------", v)

print("1" in a.keys())

## 删除
del a["1"]
print(a)

print(a.pop("2"))
print(a)

a.clear()
