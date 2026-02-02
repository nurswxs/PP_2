n = int(input())
if n <= 0:
    print("NO")
while n % 2 == 0:
    n //= 2
if n == 1:
    print("YES")
else:
    print("NO")    