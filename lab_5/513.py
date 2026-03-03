import re 

n = input()
res = re.findall(r"\w+", n)
print(len(res))