
class Student:
    schoolName = "ABC School"

    def __init__(self,name,course):
        print("Whenever a new object is created I am called automatically...")
        print(self)
        self.name=name
        self.course=course
        print(self.name)
        print(self.course)

student1 = Student("Khushi","BTech")    # __init__ method will be called
print(student1.schoolName)
print("Student1",student1.name)
print("Student1",student1.course)

student2 = Student("Ankit","BCA")
print("Student2",student2.name)
print("Student2",student2.course)
        