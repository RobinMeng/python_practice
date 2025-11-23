## 生成随机字符串
import random
import string

print(''.join(random.choices(string.ascii_letters, k=5)))
print(''.join(random.choices(string.ascii_lowercase, k=5)))
print(''.join(random.choices(string.ascii_uppercase, k=5)))

print(''.join(random.choices(string.digits, k=5)))
