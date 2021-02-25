import re

text = "13.02.1986 asd 24.24.1998 asdfkjh adsfas dasdf aadsf 01.02.2002"

pattern = "[0-9]{2}.\d{2}.\d{4}"

x = re.findall(pattern, text)
print(x)