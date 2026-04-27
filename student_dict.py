# Dictionary Examples - Student

# Creating a student dictionary
student = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# Using get() method (safer)
print("Grade:", student.get("grade"))

# Adding new key-value pair
student["city"] = "New York"
print("After adding city:", student)

# Updating existing value
student["age"] = 21
print("After updating age:", student)

# Removing items
removed_grade = student.pop("grade")
print("Removed grade:", removed_grade)
print("After pop:", student)

# Looping through dictionary
print("\nAll key-value pairs:")
for key, value in student.items():
    print(f"{key}: {value}")

# Dictionary with multiple students
students = {
    "student1": {"name": "Alice", "age": 19},
    "student2": {"name": "Bob", "age": 21}
}
print("\nMultiple students:", students)