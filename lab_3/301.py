def num(n):
    n1 = True
    for i in n:
        if int(i) % 2 != 0:
            n1 = False
            break
    if n1:
        return "Valid"
    else:
        return "Not valid"
n = input().strip()
a = num(n)
print(a)