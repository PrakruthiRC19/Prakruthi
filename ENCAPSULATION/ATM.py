class ATM:

    def __init__(self):
        self.__balance=1000 #Private variable

    def getBalance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("Deposit successfully, current balance", self.getBalance())
        else:
            print("Invalid Transaction")
    
    def withDrawl(self,amount):
        if amount>=0 and amount<=self.__balance:
            self.__balance-=amount
            print("Withdrawl successfully, current balance",self.getBalance())
        else:
            print("Invalid Transaction")

a=ATM()
print("**Initial Transaction**")
print(a.getBalance())
print("**Deposite balance**")
a.deposit(500)
print("**Withdrawl balance**")
a.withDrawl(200)