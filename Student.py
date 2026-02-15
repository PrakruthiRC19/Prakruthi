class Student:
    def __init__(self):
        self.rollNum=None
        self.name=None
s1=Student()
print("*****BEFORE VARIABLE DATA ASSIGN*****")
print(s1.rollNum)
print(s1.name)

print("*****AFTER VARIABLE DATA ASSIGN*****")
s1.rollNum=101
s1.name="Jhon"

print(s1.rollNum)
print(s1.name)

s2=Student()
print("*****BEFORE VARIABLE DATA ASSIGN*****")
print(s2.rollNum)
print(s2.name)

print("*****AFTER VARIABLE DATA ASSIGN*****")
s2.rollNum=102
s2.name="David"

print(s2.rollNum)
print(s2.name)

s3=Student()
print("*****VARIABLE DATA IS NOT ASSIGN*****")
print(s3.rollNum)
print(s3.name)


