x = 200

def f():
    global x
    x = 100
    print(x)

f()
print(x)