## 处理多个异常

def div_num(a, b):
    try:
        val = a / b
        print(val)
    except TypeError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)


div_num("hello", 3)

div_num(10000000000000000000000000000000000, 1)

div_num(1, 0)
