import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


r = int(input())
c = Circle(r)
print(f"{c.area():.2f}")
