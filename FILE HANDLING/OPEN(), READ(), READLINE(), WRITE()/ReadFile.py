class ReadFile:

    def readContent(self):

        

        file=open("learn.txt","r")
        print(file.read())
        file.close()

r=ReadFile()
r.readContent()