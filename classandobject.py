'''class attur:
    name=""
    age=""
    def party():
        print("party...")
    def lake():
        print("enjoying the lake")

yugesh= attur()
arun=attur()
yugesh.name="yugesh"
yugesh.age=23
arun.name="arun"
arun.age=22
print(yugesh.name)
print(yugesh.age)
print(arun.name)
print(arun.age)
yugesh.lake()'''
class Dog:
    species = "rott"  
    def __init__(self, name, age):
        self.name = name 
        self.age = age
dog1 = Dog("Buddy", 3)
print(dog1.name)   
print(dog1.species)  