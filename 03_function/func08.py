## inner function


def add(a, b, c):
    b = a + b
    def add_sub(b, c):
        print("inner function")
        return b + c

    return add_sub(b, c)

print(add(1, 2, 3))

