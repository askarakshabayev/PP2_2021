try:
    f = open("test.txt", "r")
    text = f.read()
except Exception as e:
    print(str(e))

print("hello world")