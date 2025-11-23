## list

num_list = list(range(10))

print(num_list)
## * 运算符
num_list2 = num_list * 3
print(num_list2)

print(len(num_list2))

## +运算符 合并列表

num_list3 = list(range(20))
num_list4 = list(range(10))
print(num_list3 + num_list4)

## 排序

num_list5 = num_list4 + num_list3
num_list5.sort()
print(num_list5)

num_list6 = num_list4 + num_list3
print(sorted(num_list6))
## 倒排
print(sorted(num_list6, reverse=True))
