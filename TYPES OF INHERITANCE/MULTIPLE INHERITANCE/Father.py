class Father:

    def drive(self):
        print("Father Knows how to drive")

class Mother:

    def cook(self):
        print("Mother Knows how to cook")

class Son(Father,Mother):
    def play(self):
        print("Son Knows how to play")

s=Son()
s.play()
s.cook()
s.drive()
 