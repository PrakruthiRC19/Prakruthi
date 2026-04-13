class WriteFile:

    def writeContent(self):

        file=open("learn.txt","w")
        print(file.write("How are you"))
        file.close()
        print("Write successfully")

w=WriteFile()
w.writeContent()