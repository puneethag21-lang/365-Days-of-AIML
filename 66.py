class student:
      def __init__(self,name,age,sem,dept):
        self.name=name
        self.age=age
        self.sem=sem
        self.dept=dept
student2=student("bob",22,4,"cse")
print(f"student: {student2.name}, Age: {student2.age}, Semester: {student2.sem}, Department: {student2.dept}")