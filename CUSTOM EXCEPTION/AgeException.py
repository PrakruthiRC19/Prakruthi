class InvalidExceptionError(Exception):
    def __init__(self):
        pass

class CheckAge:

    def validate(self,age):

        if age>=18:
            print("eligible for voting")
        else:
            raise InvalidExceptionError()
        
c=CheckAge()

try:
    c.validate(17)

except InvalidExceptionError as e:

    print(f"Age is invalid",{e})
        