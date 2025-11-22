## 随机数
import random

print(random.random())

for var in range(100):
    ## a 以上 b 一下的 int 随机数
    print(random.randint(-20, 20))
    ## a 以上 b 一下的 float 随机数
    print(random.uniform(-20, 20))

ran_list = [random.randint(-20, 20) for x in range(20)]
print("*" * 80)
print(ran_list)
print("*" * 80)
