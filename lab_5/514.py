import re

n = input()
res = re.compile(r"^\d+$")
if res.fullmatch(n):
    print("Match")
else:
    print("No match")