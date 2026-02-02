#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#2
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
#3
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
#4
nums = [3, -2, 5, -7, 8]

for n in nums:
    if n < 0:
        continue
    print(n)
#5
for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i)