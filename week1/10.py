# a, b = input().split()
# print(int(a) + int(b))

# a, b = map(int, input().split()) # '1 2' => ['1', '2'] => [1, 2] => a = 1, b = 2
# print(a + b)

a = map(int, input().split())
print(a)

for x in a:
    print(x)