n = int(input())
arr = list(map(int, input().split()))
asd = set()
for i in arr:
    if i in asd:
        print("NO")
    else:
        print("YES")
        asd.add(i)
