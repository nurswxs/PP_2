
#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#3
for i in range(1, 11):
    if i == 5:
        break
    print(i)
#4
s = "apple"

for ch in s:
    if ch == 'a':
        print("found")
        break
#5
n = 3

for i in range(1, n + 1):
    if i > 5:
        break
    print(n % i == 0)
