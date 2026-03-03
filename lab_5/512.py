import re

n = input()
res = re.findall(r"\d{2,9}", n)
print(*res)