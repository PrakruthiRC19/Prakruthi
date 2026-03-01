class BankAccount:

    def __init__(self,name,contact,age):
        self.acctHolderName=name
        self.acctHolderContact=contact
        self.acctHolderAge=age

b1=BankAccount("John",123456789,28)
print(b1.__dict__) # {'acctHolderName': 'John', 'acctHolderContact': 123456789, 'acctHolderAge': 28} directly we can print using object ref dict.