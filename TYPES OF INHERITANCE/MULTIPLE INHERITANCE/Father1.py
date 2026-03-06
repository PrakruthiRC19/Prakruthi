class Father1:

    def drive(self):
        print("Father Knows how to drive")

class Mother:

    def drive(self):
        print("Mother Knows how to drive")

    def cook(self):
        print("Mother Knows how to cook")

class Son(Father1,Mother):
    def play(self):
        print("Son Knows how to play")

class Daughter(Mother,Father1):
    def read(self):
        print("Daughter knows how to read")

print("**SON INHERIT THE PROPERTY OF FATHER AND MOTHER**")
s=Son()
s.play()
s.cook()
s.drive()

print("**DAUGHTER INHERIT THE PROPERTY FROM MOTHER**")
d=Daughter()
d.read()
d.cook()
d.drive()