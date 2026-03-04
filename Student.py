class Student:

    def __init__(self):
        self.sId=101
        self.sName="John"

s1=Student()
print(s1.sId,s1.sName) # or we can directly print the instance variable using object reference dictionary
print(s1.__dict__)