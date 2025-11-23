import random

## 倒叙函数

list_num = list(range(100))
list_num.reverse()
print(list_num)

list_num2 = list(range(100))
print(list(reversed(list(range(100)))))

print(list_num2)
print(list_num2[::-1])

## 随机打乱列表
random.shuffle(list_num2)
print(list_num2)

## 去重 dict.fromkeys

list_num3 = list(range(5))
list_num3 = list_num3 * 3
print(list_num3)
print(list(dict.fromkeys(list_num3)))
