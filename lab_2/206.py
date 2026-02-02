n = int(input())
num = list(map(int, input().split()))
max = num[0]
for i in num:
    if i > max:
        max = i
print(max)        