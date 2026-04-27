class Student:
    def __init__(self, name):
        """Initializes student details."""
        self.name = name
        self.marks = 0

    def set_marks(self, marks):
        """Validates and sets student marks (0-100)."""
        if 0 <= marks <= 100:
            self.marks = marks
        else:
            print("Invalid marks! Please enter a value between 0 and 100.")

    def get_grade(self):
        """Returns a letter grade based on marks."""
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'
    @property
    def get_prime(self):
        """Checks if the current marks value is a prime number."""
        if self.marks < 2:
            return False
        for i in range(2, int(self.marks**0.5) + 1):
            if self.marks % i == 0:
                return False
        return True
student = Student("Alice")
student.set_marks(89)
print(f"Student Name: {student.name}")
print(f"Marks: {student.marks}")
print(f"Grade: {student.get_grade()}")
print(f"Is Mark Prime?: {student.get_prime}")
