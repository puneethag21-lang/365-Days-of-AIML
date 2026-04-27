class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print("Addition:", self.a + self.b)

    def sub(self):
        print("Subtraction:", self.a - self.b)

    def mul(self):
        print("Multiplication:", self.a * self.b)

    def div(self):
        if self.b != 0:
            print("Division:", self.a / self.b)
        else:
            print("Invalid input")


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

cal = Calculator(num1, num2)

cal.add()
cal.sub()
cal.mul()
cal.div()