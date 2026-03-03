import re

s = input()

res = re.sub(r"(\d)", r"\1\1", s)

print(res)