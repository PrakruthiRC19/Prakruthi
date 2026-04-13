class FileHandling:

    def Content(self):

        try:
            with open("learn.txt","r") as r:
                print(r.read())
            try:
                with open("learn.txt","w") as w:
                    w.write("I'm currentlly leaving in BTM")

            except FileNotFoundError as e:
                print("file not found",{e})

        except FileNotFoundError as e:
            print("error",{e})  

f=FileHandling()
f.Content()
