x = 100

def f():
    def internal_f():
        print("hello world")
    
    internal_f()
    x = 200
    print(x)

f()
print(x)