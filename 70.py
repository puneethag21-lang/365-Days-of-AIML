class Student:
    school_name = "ABC University"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def display_school_name():
        print(f"university name: {Student.school_name}")
if __name__ == "__main__":
    student1 = Student("Alice", 28)
    student2 = Student("Bob", 30)
    Student.display_school_name()
    student1.display_school_name()
    student2.display_school_name()