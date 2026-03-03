import re

n = input()
res = re.findall("[0-9]", n)
print(*res)