class Animal:
    zoo="city zoo"

    def __init__(self):
        self.species="Mammal"

    def sleep(self):
        print("Animal is sleeping")

    @classmethod
    def eat(self):
        print("ANimals is eating")

    @staticmethod
    def dance():
        print("Animals is dancing")

class Dog(Animal):
    
    def bark(self):
        print("Dog is barking")

dog1=Dog()
print(dog1.species)
print(Dog.zoo)
dog1.sleep()
dog1.bark()
Dog.eat()
Dog.dance()