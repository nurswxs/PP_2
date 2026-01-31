n = int(input())
a = [input() for _ in range(n)]

first = {}
for i, s in enumerate(a):
    if s not in first:
        first[s] = i + 1

for s in sorted(first):
    print(s, first[s])
