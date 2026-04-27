import math

class Shape:
    """Base class defining a common interface."""
    def area(self): pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r**2

class Rectangle(Shape):
    def __init__(self, l, w): self.l, self.w = l, w
    def area(self): return self.l * self.w
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"{type(shape).__name__} Area: {shape.area():.2f}")
