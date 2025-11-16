## while

a = list(range(5))

num = 1

while num < len(a):
    if num % 2:
        num += 1
        continue
    if num == 4:
        break
    print(a[num])
    num += 1
