# dir
class Person:
    name = "Askar"
    param1 = 35
    param2 = 55

# print(dir(Person))

# getatr
setattr(Person, 'name', "ABC")
x = getattr(Person, 'name')
print(x)

# setatr
# hasatr