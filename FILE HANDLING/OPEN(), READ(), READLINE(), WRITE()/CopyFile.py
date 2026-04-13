class CopyFile:

    def copyContent(self):

        '''sourceFile=open("source.txt","r")

        content=sourceFile.read()

        destinationFile=open("destination.txt","w")
        
        destinationFile.write(content)

        sourceFile.close()
        destinationFile.close()'''

        with open("source.txt","r") as file:
            data=file.read()

        
        with open("destination.txt","w") as file1:
            file1.write(data)

        print("File copied successfully")

c=CopyFile()
c.copyContent()

