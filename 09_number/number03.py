## 判断两个数是否足够接近
import math

x = 1.2 - 1.0
## 绝对误差
print(math.isclose(x, 0.2))

## 相对误差
print(math.isclose(x, 0.2, rel_tol=0.001))
