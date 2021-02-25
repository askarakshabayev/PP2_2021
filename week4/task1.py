def f(n):
    a, b = 0, 1 
    # a = 1, b = 2
    for _ in range(0, n):
        yield a + b # <-
        a, b = b, a + b

