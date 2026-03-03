import re 

n = input()
pattern = r"Name: (.+), Age: (.+)"

match = re.search(pattern, n)

if match:
    name = match.group(1)
    age = match.group(2)
    print(name, age)