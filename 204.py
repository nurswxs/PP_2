n = int(input())
num = list(map(int, input().split()))
n1 = 0
for i in num:
    if i > 0:
        n1 += 1
print(n1)