class Car2:

    def assignBrand(self): # without __int__(self)
        self.brandName="MG"
    
class Windsor(Car2):
    pass

w=Windsor()
print(w)
print(w.brandName)
w.assignBrand()
