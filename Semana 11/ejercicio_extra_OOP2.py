'''
Ejercicio extra OOP2
Cree una clase base Animal y dos clases hijas Dog y Cat:
- Animal debe tener nombre y método speak() que retorne "Hace un sonido"
- Dog debe sobrescribir speak() para decir "Guau"
- Cat debe sobrescribir speak() para decir "Miau"
'''

# Define the base class Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Hace un sonido"

# Define the Dog class
class Dog(Animal):
    def speak(self):
        return "Guau"

# Define the Cat class
class Cat(Animal):
    def speak(self):
        return "Miau"
    

# Create instances of Dog and Cat
dog = Dog("Firulais")
cat = Cat("Michi")

# Print the sounds made by the dog and cat
print(f"{dog.name} dice: {dog.speak()}")
print(f"{cat.name} dice: {cat.speak()}")