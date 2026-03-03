import re

s = input()
p = input()
res = re.search(p,s)

if res:
    print("Yes")
else:
    print("No")