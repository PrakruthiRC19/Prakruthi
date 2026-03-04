class Car1:

    def __init__(self): # __init__(self) written by developer
        self.brandName="MG"
    
class Windsor(Car1): # without class logic

    pass

w=Windsor()
print(w.__dict__) 
print(w.brandName)
