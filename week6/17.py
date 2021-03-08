# isintance

# x = isinstance(5, int)
x = isinstance('hello', (float, int, str, list))

class my_obj:
    param1 = "test"

y = my_obj()
x = isinstance(y, my_obj)
print(x)