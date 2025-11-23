## 按条件提取

num_list = list(range(100))

num_filter = filter(lambda x: x % 2 == 0, num_list)
print(type(num_filter))
print(list(num_filter))
