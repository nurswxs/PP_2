import re

n = input()
n1 = input()

res = re.findall(n1,n)
print(len(res))