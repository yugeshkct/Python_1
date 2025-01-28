class Animal:
    def sound(self):
        print("animal makes sound")
class Dog(Animal):
    def sound(self):
        print("dog barks")
d1=Dog()
d1.sound()
class Bird(Animal):
    def sound(self):
        print("bird sounds")
d2=Bird()
d2.sound()
class Insect(Animal):
    def sound(self):
        print("insect sounds")
d3=Insect()
d3.sound()