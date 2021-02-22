# a = (5,)
list1 = ["Askar", "Aidar", "Madiyar", "Sholpan"]
list2 = [35, 45, 25, 18]

# a = [("Askar", 35), ("Aidar", 45), ("Madiyar", 25), ("Sholpan", 18)]
# a[0] = ("abc", 100)
# a[0][0] = "test"

# for i in range(0, len(list1)):
#     print(list1[i], list2[i])

a = [(list1[i], list2[i]) for i in range(0, len(list1))]
print(a)