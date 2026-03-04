class Animal:
    def eat(self):
        print("All animals is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class BabyDog(Dog):
    def weep(self):
        print("BabyDog is weeping")
print("\n")
print("***BABYDOG PROPERTIES***")
b=BabyDog()
b.weep()
b.bark()
b.eat()
print("\n")
print("***DOG PROPERTIES***")
d=Dog()
d.bark()
d.eat()
print("\n")
print("***ANIMAL PROPERTIES***")
a=Animal()
a.eat()