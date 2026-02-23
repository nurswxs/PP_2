#1
n = int(input())
sq = (x*x for x in range(1,n + 1))
for i in sq:
    print(i)
#2
def even(c):
    for x in range(0,c + 1):
        if x % 2 == 0:
            yield x
c = int(input())
f = True
for x in even(c):
    if not f:
        print(", ",end = "")
    print(x,end="")
    f=False
print()
#3
def divis(d):
    for x in range(0,d+1):
        if(x % 3 == 0) and (x % 4 == 0):
            yield x
d = int(input())
f = True
for x in divis(d):
    if not f:
        print(", ",end="")
    print(x,end="")
    f = False
print()
#4
def squares(a,b):
    for x in range(a,b+1):
        yield x*x
a = int(input())
b = int(input())
for val in squares(a,b):
    print(val)
#5
def down(w):
    for x in range(n,-1,-1):
        yield x
w = int(input())
for x in down(n):
    print(x)
