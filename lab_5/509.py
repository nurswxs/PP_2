import re

n = input()
res = re.findall(r"\b\w{3}\b", n)
print(len(res))