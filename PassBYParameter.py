class BookMyShow:

    def makePayment(self,ParameterType): # ParameterType is a input parameter , it is a local variable stored in stack memory.
        
        print(ParameterType,"Payment is successfull")

    # Other method of using input parameter by self keyword

    def makePayment(self,ParameterType): # ParameterType is a input parameter , it is a local variable stored in stack memory.
        self.type=ParameterType
        print(self.type,"Payment is successfull")

b=BookMyShow()
b.makePayment("UPI") # UPI Payment is successfull
b.makePayment("CREDITCARD") # CREDITCARD Payment is successfull
b.makePayment("CASH") # CASH Payment is successfull

print(b.__dict__) # {'type': 'CASH'}

b.type("internetbanking")