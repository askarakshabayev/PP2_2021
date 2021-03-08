# enumerate(iterable, start=0)

x = ['abc', 'def', 'lll']

enumx = enumerate(x, 10)

# for item in enumx:
#     print(item)
for i, item in enumx:
    print(i, item)