from abc import ABC, abstractmethod
class Operation(ABC):
    @abstractmethod
    def calculate(self, x, y):
        """Perform a mathematical operation."""
        pass
class Addition(Operation):
    def calculate(self, x, y):
        return x + y
class Subtraction(Operation):
    def calculate(self, x, y):
        return x - y
class Multiplication(Operation):
    def calculate(self, x, y):
        return x * y
class Division(Operation):
    def calculate(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y
def get_result(operation_obj, a, b):
    print(f"Result: {operation_obj.calculate(a, b)}")

add = Addition()
sub = Subtraction()
mul = Multiplication()
div = Division()
num1=int(input("enter first number:  "))
num2=int(input("enter second number:  "))
