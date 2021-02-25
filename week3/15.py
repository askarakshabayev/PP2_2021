import re
# t = "abc23lllm4596pp2342"

# x = re.findall("[0-9]+", t)
# print(x)

t = "askar@1fit.app askar__aa_a@gmail.com askar"

x = re.findall(r"[a-z0-9_]+@[a-z]+\.[a-z]{2,5}", t)
print(x)