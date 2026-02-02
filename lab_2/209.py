n = int(input())
arr = list(map(int, input().split()))
maxi = max(arr)
mini = min(arr)

for i in range(n):
    if arr[i] == maxi:
        arr[i] = mini
print(*arr)