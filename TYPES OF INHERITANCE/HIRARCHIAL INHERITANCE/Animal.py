class Animal:
    def eat(self):
        print("All animals is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meow")

class Lion(Animal):
    def roar(self):
        print("LIon is roaring")

print("\n")
print("***LION PROPERTIES***")
l=Lion()
l.roar()
l.eat()
print("\n")
print("***CAT PROPERTIES***")
c=Cat()
c.meow()
c.eat()
print("\n")
print("***DOG PROPERTIES***")
d=Dog()
d.bark()
d.eat()
print("\n")
print("***ANIMAL PROPERTIES***")
a=Animal()
a.eat()