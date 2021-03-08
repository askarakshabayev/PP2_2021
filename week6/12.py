# filter(function, iterable)

letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

def filter_vowels(letter):
    if letter in ['a', 'e', 'i', 'o', 'u']:
        return True
    return False

vowels_letters = filter(filter_vowels, letters)

for item in vowels_letters:
    print(item)
