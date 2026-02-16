#1
class aa:
    x = 5
bb = aa()
print(bb.x)
#2
class phone:
    brand = "iphone"
    year = 2026
c = phone()
print(c.brand, c.year)
#3
class Empty:
    pass
e = Empty()
print(type(e))
#4
class game:
    boss = "666 HP"
class werty:
    collection = game()
v = werty()
print(v.collection.boss)
#5
class group:
    students = ["Werty", "Niaven", "Goose"]
sg = group()
print(*sg.students)