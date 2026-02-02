n = int(input())
eps = {}

for _ in range(n):
    s, k = input().split()
    k = int(k)
    if s in eps:
        eps[s] += k
    else:
        eps[s] = k
for s in sorted(eps):
    print(s, eps[s])
