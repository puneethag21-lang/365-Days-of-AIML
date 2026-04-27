import math
from collections import defaultdict

class Triangle:
    def __init__(self, base, height): self.base = base; self.height = height
    @property
    def area(self): return 0.5 * self.base * self.height

class Rectangle:
    def __init__(self, length, width): self.length = length; self.width = width
    @property
    def area(self): return self.length * self.width

class Circle:
    def __init__(self, radius): self.radius = radius
    @property
    def area(self): return math.pi * (self.radius ** 2)

shapes_info = defaultdict(lambda : 'Invalid dimensions')
t = Triangle(5, 6)       # triangle with base=5 and height=6
r = Rectangle(4, 7)      # rectangle with length=4 and width=7
c = Circle(3)           # circle with radius=3

shapes_info['triangle'] = round((t.area),2) if 'invalid' not in shapes_info.values() else t.__dict__["area"]
shapes_info['rectangle'] = r.area
shapes_info['circle']   = math.pi * c.radius ** 2 or c.__dict__["area"]
print("Shapes information:", dict(shapes_info))