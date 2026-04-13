class ReadFile:

    def readContent(self):

        file=open("learn.txt","r")
        print(file.readline())
        print(file.readline())
        file.close()

r=ReadFile()
r.readContent()
