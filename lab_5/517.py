import re 

n = input()
res = re.findall(r"(\d{2})/(\d{2})/(\d{4})", n)
print(len(res))