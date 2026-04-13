class Test:

    def __init__(self):
        self.x=10
        self.__y=20

class RunTest:

    def run(self):
        print("Public variable:",Test.x)

        print("Private variable:",Test._Test__y)
        print("Private variable:",Test.__y)

# or

t=Test()
print(t._Test__y)