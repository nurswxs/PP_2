n = int(input())
arr = list(map(int, input().split()))
prime = {}
for i in arr:
    if i in prime:
        prime[i] += 1
    else:
        prime[i] = 1
max_prime = max(prime.values())
ans = min(x for x in prime if prime[x] == max_prime)
print(ans)
