# double all elements in list (using map)

list1 = [2, 5, 10, 100, 103, 201] # 4, 10, 20, 200, 206, 402

list2 = list(map(lambda x: x ** 2, list1))

print(list2)

