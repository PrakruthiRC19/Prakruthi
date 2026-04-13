from abc import ABC, abstractmethod

class Payment:

    @abstractmethod #incomplete method
    def makePayment(self,amount):
        pass

class creditCardPayment(Payment):

    def makePayment(self, amount):#complete method
        print(f"procession credit card payment {amount}...")

class UPI(Payment):

    def makePayment(self, amount):#complete method
        print(f"procession UPI payment {amount}...")

c=creditCardPayment()
c.makePayment(100)

u=UPI()
u.makePayment(200)

p=Payment()
# p.makePayment() #cannot create object of abstract class