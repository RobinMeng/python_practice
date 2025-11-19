## 对外抛异常

def div_num(a, b):
    try:
        val = a / b
    except BaseException as e:
        print(e)
        raise e


div_num(1, 0)
