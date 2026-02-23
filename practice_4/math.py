import math
d = float(input())
n = d * math.pi / 180
print(n)
#2
height = float(input())
base1 = float(input())
base2 = float(input())
area = (height*(base1 + base2)) / 2
print(area)
#3
s = int(input())
l = float(input())
area = (s * l**2) / (4 * math.tan(math.pi / s))
print(area)
#4
b = float(input())
h = float(input())
ar = b * h
print(ar)
