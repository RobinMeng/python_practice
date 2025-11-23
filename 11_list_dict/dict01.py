## 生成k-v dist
import random
import string

num_list = list(range(10))

key = ''.join(list(random.choices(string.ascii_letters, k=3)))
key_list = [''.join(list(random.choices(string.ascii_letters, k=3))) for x in num_list]
print(num_list)
print(key_list)
zip_num = zip(key_list, num_list)
dict_num = dict(zip_num)
print(dict_num)

## 交换字典中的kv

dict_vk = {v: k for k, v in dict_num.items()}
print(dict_vk)
## 合并两个字典
dict_num.update(dict_vk)
print(dict_num)

