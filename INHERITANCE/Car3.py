class Car3:

    def __init__(self): # 
        self.model="2025"

    def assignBrand(self):
        self.brandName="MG"

class Windsor(Car3):
    
    def __init__(self):
        self.enginCountry="British"

w=Windsor()
print("BEFOR",w.__dict__) # {'enginCountry': 'British'}
w.assignBrand() # {'enginCountry': 'British', 'brandName': 'MG'}
print("AFTER",w.__dict__)
