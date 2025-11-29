## 简单线程
import threading
import time


def print_num():
    print("数字{}", 1)
    time.sleep(10)


if __name__ == '__main__':
    print(print_num)
    print(print_num())
    thread = threading.Thread(target=print_num)
    print("线程开始执行")
    thread.start()
    thread.join()
    print("线程执行结束")
