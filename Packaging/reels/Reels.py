import login.SignIn as s

class Reels:

    def createReels(self,content):
        signin=s.SignIn("prakruthi","praku19")
        signin.signIn()
        print("creating a reels content:",content)

    def shareReels(self,reel_id):
        print("sharing reels with Id:",reel_id)

reel=Reels()
reel.createReels("My new reel content")
reel.shareReels("praku@19")