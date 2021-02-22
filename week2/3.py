def func(*args):
    for arg in args:
        print(arg, type(arg))

func([1, 2, 3], "hello", 15)