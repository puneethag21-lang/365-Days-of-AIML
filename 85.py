from abc import ABC, abstractmethod
import math

# 1. Abstract Base Class (Abstraction)
class Shape(ABC):
    @abstractmethod
    def area(self): pass

# 2. Subclasses (Inheritance)
class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height): self.width, self.height = width, height
    def area(self): return self.width * self.height

# 3. Simple Calculator Class
class Calculator:
    def add(self, a, b): return a + b
    def div(self, a, b): return a / b if b != 0 else "Err"

# --- Demo (Polymorphism & Objects) ---
shapes = [Circle(5), Rectangle(4, 6)]
for s in shapes: print(f"{type(s).__name__} Area: {s.area():.2f}")

calc = Calculator()
print(f"10+5 = {calc.add(10, 5)}")
