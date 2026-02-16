#1
class Human:
    def __init__(self, n):
        self.n = n

class Learner(Human):
    def __init__(self, n, s):
        super().__init__(n)
        self.s = s

a = Learner("Werty", "IT")
print(a.n, a.s)
#2
class Beast:
    def sound(self):
        print("Noise")

class Hound(Beast):
    def sound(self):
        super().sound()
        print("Bark")

Hound().sound()
#3
class Machine:
    def __init__(self, m):
        self.m = m

class Auto(Machine):
    def __init__(self, m, y):
        super().__init__(m)
        self.y = y

b = Auto("X", 2020)
print(b.m, b.y)
#4
class Main:
    def show(self):
        print("Main")

class Sub(Main):
    def show(self):
        super().show()
        print("Sub")

Sub().show()
#5
class Core:
    def __init__(self, v=0):
        self.v = v

class Ext(Core):
    def __init__(self, v, u):
        super().__init__(v)
        self.u = u

c = Ext(1, 2)
print(c.v, c.u)
