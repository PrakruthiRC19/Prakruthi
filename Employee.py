class Employee:
    CompanyName="DCL" # class variable , stored in class object memory

    def __init__ (self):
        self.empid=None
        self.empname=None
        print(self)

print(Employee.CompanyName)

e1=Employee() # we can create a abject without self keyword.

e1.CompanyName="Google" # we can modify the class variable by using object reference, that will be store in object.

print(e1)
print(e1.CompanyName)

print(Employee.CompanyName)

print(Employee)

e1.salary=10000
print(e1.salary)

Employee.CompanyName="meta" #we can also modify class variable by using class name

print(Employee.CompanyName) 


