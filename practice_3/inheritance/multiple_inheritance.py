#1
class A:
    a = 1

class B:
    b = 2

class R(A, B):
    pass

r = R()
print(r.a, r.b)
#2
class First:
    def __init__(self):
        print("First")

class Second:
    def __init__(self):
        print("Second")

class Both(First, Second):
    def __init__(self):
        First.__init__(self)
        Second.__init__(self)
        print("Both")

Both()
#3
class Alpha:
    def hi(self):
        print("Hi Alpha")

class Beta:
    def hi(self):
        print("Hi Beta")

class Gamma(Alpha, Beta):
    def hi(self):
        super().hi()
        print("Hi Gamma")

Gamma().hi()

class Gamma(Beta, Alpha):
    def hi(self):
        super().hi()
        print("Hi Gamma")

Gamma().hi()
#4
class Top:
    def show(self):
        print("Top")

class Left(Top):
    def show(self):
        print("Left")

class Right(Top):
    def show(self):
        print("Right")

class Bottom(Left, Right):
    pass

Bottom().show()
