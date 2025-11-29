## lock
import threading

num = 0
lock = threading.Lock()


def add_num_un_safe(start, end):
    global num
    for var_num in range(start, end):
        num += var_num


def add_num_safe(start, end):
    global num
    for var_num in range(start, end):
        with lock:
            num += var_num


def un_safe_test():
    """
    加法次数要尽可能多 才可以看出效果,每次结果不一致
    :return:
    """
    thread1 = threading.Thread(target=add_num_un_safe, args=[1, 1000000])
    thread2 = threading.Thread(target=add_num_un_safe, args=[1000001, 2000001])
    thread3 = threading.Thread(target=add_num_un_safe, args=[2000001, 3000001])
    thread4 = threading.Thread(target=add_num_un_safe, args=[3000001, 4000001])
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    print(f"un_safe_test 最终结{num}")


def safe_test():
    """
    每次结果不一致
    :return:
    """
    thread1 = threading.Thread(target=add_num_safe, args=[1, 1000000])
    thread2 = threading.Thread(target=add_num_safe, args=[1000001, 2000001])
    thread3 = threading.Thread(target=add_num_safe, args=[2000001, 3000001])
    thread4 = threading.Thread(target=add_num_safe, args=[3000001, 4000001])
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    print(f"safe_test 最终结{num}")


if __name__ == '__main__':
    un_safe_test()
    num = 0
    safe_test()
