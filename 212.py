n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    arr[i]**= 2
print(*arr)