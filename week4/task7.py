import re

text = "abc2342asdf234fassdf34"

numbers = re.findall("[0-9]+", text)

print(numbers)