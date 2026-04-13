class A:

    def __init__(self):
        self.x=10
        self._y=20

import Folder1.A as a

class B(a.A):

    def printDate(Self):
        pass
b= B()
b.printDate()
print(b._y)