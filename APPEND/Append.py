class Append:

    def appendContent(self):

        with open ("learn.txt","a") as file:
            file.write("I'm prakruthi , I'm getting training in DCL")

a=Append()
a.appendContent()