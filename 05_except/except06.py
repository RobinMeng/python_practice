## 发生异常时详细信息字符串
import traceback


def div_num(a, b):
    try:
        val = a / b
    except:
        print("错误信息\n" + traceback.format_exc())


div_num(1, 0)
