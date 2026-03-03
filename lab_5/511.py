import re

n = input()
res = re.findall("[A-Z]", n)
print(len(res))