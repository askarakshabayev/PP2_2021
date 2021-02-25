import re
text = "faslkjfh afkadjh asdfjh 20BD13999 asdfasdf asdfas 20BD156 asdfhkjasd asdfasd 20BD2020"
pattern = r"20BD\d+"

x = re.findall(pattern, text)
print(x)