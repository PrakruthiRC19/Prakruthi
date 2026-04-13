class LoveException(Exception):

    def __init__(self, message):
        super().__init__(message)

class P:

    def expressLove(self,bF):
        if bF=="S":
            print("I love you S")
        else:
            raise LoveException("sorry")
        
p=P()
        
try:
    p.expressLove("S")
except LoveException as e:
    print(e)
else:
    print("proposal is accepted") # only if try block is excepted successfully 
finally:
    print("Marriage not happens")