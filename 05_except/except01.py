def div_num(a: int, b: int) -> None:
    try:
        val = a / b
        print(val)
    except BaseException as e:
        print(e)

div_num(1, 2)

div_num(1, 0)
