class DMART:

    discountOfEachProduct=0.01

    def __init__(self):
        self.gstn=None
        self.location=None

    def calculatePrice(self, prodName, originalPriceOfProduct):
        actualPrice=originalPriceOfProduct-(originalPriceOfProduct*DMART.discountOfEachProduct)
        print("Actual price of",prodName , "after discount",actualPrice)

    @classmethod
    def revisedDiscount(cls,newDiscount):
        cls.discountOfEachProduct=newDiscount

print("***PRICE OF DEFAULT DISCOUNT***")
d1=DMART()
d1.gstn=12345678
d1.location="BTM"
d1.calculatePrice("prestige cooker",5000)

d2=DMART()
d2.gstn=12345678
d2.location="BTM"
d2.calculatePrice("philips airflyer",8000)

DMART.revisedDiscount(0.20)
print("***PRICE WITH REVISED DISCOUNT DUE TO FESTIVAL***")
d1.calculatePrice("prestige cooker",5000)
d2.calculatePrice("philips airflyer",8000)
