class SignIn:

    def __init__(self,username,password):
        self.username=username
        self.password=password

    def signIn(self):
        print("signing in with username",self.username ,"and password", self.password)

    def dummyFunc(self):
        print("This is dummy function in SignIn class")

