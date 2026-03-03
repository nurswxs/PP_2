import re

n = input()
s = re.match("Hello", n)
if s:
    print("Yes")
else:
    print("No")