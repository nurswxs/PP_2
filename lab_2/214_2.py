n = int(input())
arr = list(map(int, input().split()))
maxi = arr[0]
count = 0
for i in range(n):
    if maxi == arr[i-1]:
        maxi == arr[i]
        count += 1
print(maxi)
print(count)
