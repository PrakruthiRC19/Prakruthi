class InsufficientBalanceException(Exception):
    def __init__(self):
        pass

class Balance:
    
    def __init__(self):
        self.__balance=5000
    
    def withdraw(self,amount):

        if amount>=0 and amount<=self.__balance:
            self.__balance-=amount
            print("Withdrawl successfully, current balance" , self.__balance)
        else:
            raise InsufficientBalanceException()
        
b=Balance()
 
try:
    
    b.withdraw(4000)

except InsufficientBalanceException as e:

    print(f"Insufficient Balance",{e})