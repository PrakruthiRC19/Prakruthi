class Parent:

    x=20 

    def __init__(self):
        print("I am in Parent init")
        self.x=10

    def show(self):
        print("I am in Parent class")

class Child(Parent):

    def display(self):
        
        super().show()
        super().__init__()
        # print(super().x) #'super' object has no attribute 'x' , we can't access instance variable using super()
        print(self.x) # can access instance method in child class
        print(super().x) # we can access class variable using super()

c=Child() # when obj is created variables are initialized so it print 1st __init__ then it execute child class
c.display()
