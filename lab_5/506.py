import re

n = input()
res = re.search("\S+@\S+\.\S+", n)
if res:
    print(res.group())
else:
    print("No email")