set1 = set()
set1.add(1)
set1.add(2)
set1.add(3)

try:
    set1.remove(10)
except Exception as arg:
    print("Error", str(arg))
print("hello world")
# set1.discard(10)

print(set1)