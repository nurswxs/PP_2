n = int(input())
num = list(map(int, input().split()))
max = num[0]
pos = 1
for i in range(1,n):
    if num[i] > max:
        max = num[i]
        pos = i + 1
print(pos)