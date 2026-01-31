n,l,r = map(int, input().split())
arr = list(map(int, input().split()))
arr[l - 1:r] = arr[l - 1:r][::-1]
print(*arr)