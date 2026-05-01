class Animal :
    Breed = "Labrador"

    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Saying now ......")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")

a = Animal("Sheru")
a.speak()

b = Dog("Dogesh")
b.speak()
print(b.Breed)