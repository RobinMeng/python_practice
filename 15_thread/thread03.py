## Semaphore 允许同时并发线程的数量，N=1 将为互斥锁，执行完毕后 release 还回去
import threading

semaphore = threading.Semaphore(2)


def print_num(start, end):
    with semaphore:
        threadmsg = threading.currentThread()
        for var_num in range(start, end):
            print(f"{threadmsg.name}----var_num:{var_num} \n")


def print_num_test():
    thread1 = threading.Thread(target=print_num, args=[1, 1000])
    thread2 = threading.Thread(target=print_num, args=[1001, 2001])
    thread3 = threading.Thread(target=print_num, args=[2001, 3001])
    thread4 = threading.Thread(target=print_num, args=[3001, 4001])
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()


if __name__ == '__main__':
    print_num_test()
