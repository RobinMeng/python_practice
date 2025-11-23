## 对list 元素特定处理

num_list = list(range(20))
## map函数 非k-v 结构
num_map = map(lambda a: a * 2, num_list)

print(list(num_map))
