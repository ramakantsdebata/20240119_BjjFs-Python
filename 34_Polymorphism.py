class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this.")
    
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Woof!"
    
class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Meow!"
    
class Cow:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Moo!"
    

def animal_noise(animal: Animal):
    print(animal.speak())
       
fido = Dog("Fido")
isis = Cat("Isis")
moo = Cow("Moo")

animal_noise(fido)
animal_noise(isis)
animal_noise(moo)