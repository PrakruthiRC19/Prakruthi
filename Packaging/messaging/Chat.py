import login.SignIn as s

class Chat:

    si=s.SignIn("prakruthi","praku19")

    def sendMessage(self,message):
        Chat.si.signIn()
        print("sending message:",message)

    def displayUserName(Self):
        print("Displaying username in chat", Chat.si.username)

c=Chat()
c.sendMessage("Hello, How are you")
c.displayUserName()