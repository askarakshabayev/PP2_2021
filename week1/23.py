a = [1, 2, 3]
b = [5, 6, 7]
a.extend(b)
p = a.index(6)
print(p)
a.insert(1, "hello")
a.remove("hello")
print(a)