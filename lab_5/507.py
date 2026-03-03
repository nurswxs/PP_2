import re

n = input()
n1 = input()
n2 = input()
res = re.sub(n1, n2, n)
print(res)