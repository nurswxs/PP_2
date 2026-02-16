#1
class Person:
    def __init__(self, n):
        self.n = n

    def greet(self):
        print("Hello, my name is " + self.n)

a = Person("Werty")
a.greet()
#2
class Math:
    def square(self, n):
        return n * n

print(Math().square(2))
#3
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

c = Rectangle(2, 3)
print(c.area())
#4
class Counter:
    def __init__(self):
        self.n = 0

    def inc(self):
        self.n += 1

d = Counter()
d.inc()
w = Counter()
w.inc()
w.inc()
print(d.n)
print(w.n)
#5
class Student:
    def __init__(self, n):
        self.n = n

    def intro(self, s):
        print(f"My name is {self.n}, I study {s}.")

e = Student("Werty")
e.intro("IT")