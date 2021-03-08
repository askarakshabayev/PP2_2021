def z():
    print("Hello world")

def z1():
    print("hi hi")

def f(x):
    if callable(x):
        x()
    else:
        print(x)

# p = "hi"
# f(p)
f(z)


# d = {"func1": z, "func2": z1}
# d['func2']()