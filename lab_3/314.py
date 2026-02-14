n = int(input())
arr = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    parts = input().split()
    op = parts[0]
    
    if op == "add":
        x = int(parts[1])
        arr = list(map(lambda a: a + x, arr))
    elif op == "multiply":
        x = int(parts[1])
        arr = list(map(lambda a: a * x, arr))
    elif op == "power":
        x = int(parts[1])
        arr = list(map(lambda a: a ** x, arr))
    elif op == "abs":
        arr = list(map(lambda a: abs(a), arr))

print(*arr)
