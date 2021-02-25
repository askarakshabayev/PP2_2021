from datetime import datetime

now = datetime(.now())

print(now)
print(now.day)
print(now.year)
print(now.month)
print(now.strftime("%m:%Y"))

now = datetime(2018, 3, 15)

print(now.strftime("%A"))