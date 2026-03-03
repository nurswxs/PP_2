import re

n = input()
n1 = input()

res = re.escape(n1)
a = re.findall(res, n)
print(len(a))