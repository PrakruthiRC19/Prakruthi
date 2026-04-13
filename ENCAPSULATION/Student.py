class Student:

    def __init__(self):
        self.StuId=101
        self.__stuMarks=50

    def getStuMarks(self):
        return self.__stuMarks
    
    def setStuMarks(self,marks):
        if marks>=0 and marks<=100:
            self.__stuMarks=marks
            print("Marks updated successfully, Current Marks", self.getStuMarks())
        else:
            print("Invalid marks")

class Teacher:

    def modifyMarks(self,StudentObjectAddress,marks):
        StudentObjectAddress.setStuMarks(marks)

s=Student()
print("Initial Marks")
print(s.getStuMarks())
t=Teacher()
t.modifyMarks(s,80)
    
        