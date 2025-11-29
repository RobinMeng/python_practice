## thread pool
import concurrent.futures as futures
import threading

executor = futures.ThreadPoolExecutor(max_workers=10)
future_list = []
for _ in range(100):
    future = executor.submit(lambda: print(f"hello,{threading.currentThread().name}\n"))
    future_list.append(future)

for future in future_list:
    print("*" * 100)
    print(future.result())

## python 高阶写法
with executor:
    executor.map(lambda _: print(f"hello,map {threading.currentThread().name}\n"), range(100))
