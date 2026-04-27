import math
class Triangle:
    def __init__(self, b, h): self.b, self.h = b, h
    def area(self): return 0.5 * self.b * self.h
class Rectangle:
    def __init__(self, l, w): self.l, self.w = l, w
    def area(self): return self.l * self.w
class Circle:
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r * self.r
t = Triangle(5, 6)
r = Rectangle(4, 7)
c = Circle(3)
print("Triangle area:", t.area())
print("Rectangle area:", r.area())
print("Circle area:", round(c.area(), 2))
