class BookMyShow:

    def makePayment(self):
        print("payment is successfull")

b=BookMyShow()

print(b.__dict__)

b.makePayment()

print(b.__class__) #<class '__main__.BookMyShow'>

print(b.__class__.__dict__) #{'__module__': '__main__', 'makePayment': <function BookMyShow.makePayment at 0x000001988A06A5E0>, '__dict__': <attribute '__dict__' of 'BookMyShow' objects>, '__weakref__': <attribute '__weakref__' of 'BookMyShow' objects>, '__doc__': None}

print(b.__class__.__dict__['makePayment']) #<function BookMyShow.makePayment at 0x000001988A06A5E0>

    