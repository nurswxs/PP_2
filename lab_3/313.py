from math import isqrt

nums = list(map(int, input().split()))

is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, isqrt(x)+1))

primes = list(filter(is_prime, nums))

if primes:
    print(*primes)
else:
    print("No primes")
