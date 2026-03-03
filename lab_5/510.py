import re

n = input()
res = re.search("cat|dog", n)
if res:
    print("Yes")
else:
    print("No")