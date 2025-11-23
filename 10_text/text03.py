## 替换字符串

var = 'today is $data, my name is $name'

data = 10
name = 'test'

print(var.replace('$data', str(data)).replace('$name', name))

## 判断字符串中是否包含某个字符串

var2 = 'this is a pen'
result = 'pen' in var2
print(result)
print("*" * 50)
print(var2[0:])
print(var2[:])
print(var2[0:3])

## 去除空格
var3 = ' this is a pen '
## 去除两侧空格
print(var3.strip())
## 去除左侧空格
print(var3.lstrip())
## 去除右侧空格
print(var3.rstrip())

## 大小写转换

print(var3.upper())
print(var3.upper().lower())

## 判断字符串类型
## is...
var4 = '1'
print(var4.isnumeric())
print(var4.isalnum())

var5 = 'this is a pen'
var5_list = var5.split(" ")
print(var5_list)
