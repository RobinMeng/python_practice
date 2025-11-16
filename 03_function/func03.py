## 在函数调用中指定位置参数
### 相加
def add(a, b, c):
    return a + b + c


params = [2, 3, 4]
print(add(2, 3, 4))
## 指定列表参数 *param
print(add(*params))

## 指定字典参数
params_map = {"a": 2, "b": 3, "c": 4}
print(add(**params_map))


## 混用
def sub(a, b, c, d, e, f):
    return a - b + c - d + e - f

list_param = [10, 1, 3]
dict_param = {"d": 1, "e": 2, "f": 3}

print(sub(*list_param, **dict_param))
