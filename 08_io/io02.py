## with open 上下文 会主动关闭 io

with open('./data.txt', encoding='utf-8') as f:
    print(f.read())

with open('./data.txt', encoding='utf-8') as f:
    print("*" * 50)
    print(f.readlines())

with open('./data.txt', encoding='utf-8') as f:
    print("*" * 50)
    print(f.readline())
