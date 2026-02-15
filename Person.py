class Person:
    def __init__(self):
        self.PersonID=None
        self.PersonName=None

p1=Person()
print("*****BEFORE VARIABLE DATA ASSIGN*****")
print(p1.PersonID)
print(p1.PersonName)

print("*****AFTER VARIABLE DATA ASSIGN*****")
p1.PersonID=101
p1.PersonName="Prakruthi"

print(p1.PersonID)
print(p1.PersonName)

p2=Person()
print("*****BEFORE VARIABLE DATA ASSIGN*****")
print(p2.PersonID)
print(p2.PersonName)

print("*****AFTER VARIABLE DATA ASSIGN*****")
p2.PersonID=102
p2.PersonName="Sachin"

print(p2.PersonID)
print(p2.PersonName)


