class Animal:

    def makeSound(self):
        print("Animals makes a sound")

class Dog(Animal):

    def makeSound(self): #Overriding method 
        super().makeSound()

a=Animal()
a.makeSound() #Animal makes a sound

d=Dog()
d.makeSound() #Bow Bow