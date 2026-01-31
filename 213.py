n = int(input())
arr = 0

for i in range(1, n + 1):
    if n % i == 0:
        arr += 1

if arr == 2:
    print("Yes")
else:
    print("No")
