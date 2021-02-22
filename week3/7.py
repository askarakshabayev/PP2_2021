class MyClass:
    # fields
    x = 5
    y = 6

    # methods
    def sum(self, a, b):
        return self.x + self.y + a + b

a = MyClass() # a.x, a.y
a.x = 10
a.y = 20

b = MyClass() # b.x, b.y
b.x = 7
b.y = 30

print(a.x, a.y)
print(b.x, b.y)
print(a.sum(1, 2)) # 
print(b.sum(3, 4)) # b.x + b.y

