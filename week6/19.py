# map (function, iterable)

# def f(s):
#     return len(s)

# x = map(f, ('hello', 'aa', '123456789'))
# print(list(x))

def f(a, b):
    return a + b

x = map(f, ('abc', '123', 'ppp'), ('hello', 'world', 'ttt'))
print(list(x))