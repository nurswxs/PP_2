#1
class Beast:
    def sound(self):
        print("Noise")

class Kitty(Beast):
    def sound(self):
        print("Meow")

Kitty().sound()
#2
class Form:
    def area(self):
        return 0

class Quad(Form):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2

print(Quad(2).area())
#3
class Human:
    def hi(self):
        print("Hi")

class Pupil(Human):
    def hi(self):
        print("Hi, pupil")

Pupil().hi()
#4
class Ride:
    def speed(self):
        return '30 km per hour'

class Auto(Ride):
    def speed(self):
        return '60 km per hour'

print(Auto().speed())
#5
class Wallet:
    def take(self, x):
        print(f"Take {x}")

class Safe(Wallet):
    def take(self, x):
        if x > 5:
            print("Too much")
        else:
            super().take(x)

Safe().take(3)
Safe().take(7)
