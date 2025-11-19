## 断言

def abs_sum(a, b):
    """求绝对值之和(存在错误)"""
    val = abs(a) + b
    assert val >= 0, "计算结果为负数"
    return val


print(abs_sum(-100, 200))

print(abs_sum(-100, -200))
