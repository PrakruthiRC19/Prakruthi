class Test:

    def verifyUser(func_name): # creating of decorators
        
        def wrapper_name(self):
            print("Verifying user....")
            func_name(self)
            print("User has completed the operation , logged out successfully")
        return wrapper_name
    
    @verifyUser

    def StartTest(self):
        print("Student started the test.")

    @verifyUser

    def applyForHallticket(self):
        print("Student applied for Hall ticket.")

t=Test()

t.applyForHallticket()

t.StartTest()