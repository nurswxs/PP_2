#1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Person("Werty", 18)
print(a.name, a.age)
#2
class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

b = Book("Theory of everything")
print(b.title, b.author)
#3
class Classroom:
    def __init__(self, students):
        self.students = students

c = Classroom(["Miko", "Zheks"])
print(c.students)
#4
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14 * radius * radius

circle = Circle(5)
print(circle.radius, circle.area)
#5
class Laptop:
    def __init__(self, brand, price, year):
        self.brand = brand
        self.price = price
        self.year = year

l = Laptop("Zenbook", 1200, 2024)
print(l.brand, l.price, l.year)