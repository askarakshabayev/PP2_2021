# user = dict()
# user["fname"] = "Askar"
# user["lname"] = "Akshabayev"

# print(user["fname"])

# for key in user:
#     print(key, user[key])

# if "fname" not in user:
#     print("YES")
# else:
#     print("NO")

# 1, 2, 1, 2, 100, 100, 100, 1
# 1 - 3
# 2 - 2
# 100 - 3
list1 = [1, 2, 1, 2, 100, 100, 100, 1]
a = dict()

for i in list1:
    if i not in a:
        a[i] = 0
    a[i] += 1

print(a)
