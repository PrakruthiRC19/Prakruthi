class Employee:
    
    def __init__ (self):
        salary=10000 # local variable stored in stack (temparary memory)
        print(salary) # we have to access local variable inside the function.
        print("***End***")

    print("***outside the init the local variable not accessable***")

e1=Employee()

print("***outside the class the local variable not accessable***")

