"""
try-except-else-finally 执行
"""


def div_num(a, b):
    try:
        val = a / b
        print(val)
    except BaseException as e:
        print("error", e)
    else:
        print("数据正常")
    finally:
        print("最终处理")


div_num(1, 2)
print("*" * 30)
div_num(7, 0)
