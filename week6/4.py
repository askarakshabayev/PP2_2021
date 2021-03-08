numbers = [1, 3, 2, 5, 7]

def is_even(n):
    if n % 2 == 0:
        return True
    return False

print(any(is_even(number) for number in numbers))