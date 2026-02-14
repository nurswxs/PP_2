def isUsual(num):
    if num <= 0:
        return False

    for prime in [2, 3, 5]:
        while num % prime == 0:
            num //= prime

    return num == 1


n = int(input())

if isUsual(n):
    print("Yes")
else:
    print("No")
