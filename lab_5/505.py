import re

n = input()
res = re.search("^[a-zA-Z]" and "[0-9]$", n)
if res:
    print("Yes")
else:
    print("No")