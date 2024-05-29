class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print('student name is ',self.name)
        print('student roll no is ',self.rollno)
        print('student marks',self.marks)

s1=Student('shankar',111,11)
s1.display()
