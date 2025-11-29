## condition 条件
import threading
import random
import time
import string

lock = threading.Lock()
producerCondition = threading.Condition(lock)
consumerCondition = threading.Condition(lock)

mq = []


def producer(msg):
    while True:
        with producerCondition:
            while len(mq) >= 10:
                print("*" * 100)
                print("producer 进入等待时间")
                producerCondition.wait()
                print("producer 被唤醒了")
                print("*" * 100)
            time.sleep(random.uniform(0.1, 0.5))
            mq.append(msg)
            print(f"产生数据{msg}")
            consumerCondition.notify_all()


def customer():
    while True:
        with consumerCondition:
            while not mq:
                print("*" * 100)
                print("consumer 进入等待时间")
                consumerCondition.wait()
                print("consumer 被唤醒了")
                print("*" * 100)
            time.sleep(random.uniform(0.3, 0.6))
            msg = mq.pop()
            print(f"消费数据{msg}")
            producerCondition.notify_all()


def test_condition():
    producer_thread = threading.Thread(target=producer, args=["".join(random.choices(string.ascii_letters, k=5))])
    consumer_thread = threading.Thread(target=customer)
    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
    consumer_thread.join()


if __name__ == '__main__':
    test_condition()
