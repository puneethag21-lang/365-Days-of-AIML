#write  a python code to create  a student class with properties name ,age ,sem,marks department ,phnoe no,address
class student:
      def __init__(self,name,age,sem,dept,phone,address,marks):
        self.name=name
        self.age=age
        self.sem=sem
        self.dept=dept
        self.phone=phone 
        self.address=address
        self.marks=marks
student2=student("bob",22,4,"cse",1234567890,"123 Main St",85)
print(f"student: {student2.name}, Age: {student2.age}, Semester: {student2.sem}, Department: {student2.dept}, Phone: {student2.phone}, Address: {student2.address}, Marks: {student2.marks}")