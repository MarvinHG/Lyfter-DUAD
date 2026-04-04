'''
Ejercicios de OOP #2
Cree una clase de Bus con:
Un atributo de max_passengers.
Un método para agregar pasajeros uno por uno 
(que acepte como parámetro una instancia de la clase Person vista en la lección). 
Este solo debe agregar pasajeros si lleva menos de su máximo. 
Sino, debe mostrar un mensaje de que el bus está lleno.
Un método para bajar pasajeros uno por uno (en cualquier orden).
'''

# Create a class called "Bus" to manage passengers.
class Bus:
    # Initialize the class with the maximum number of passengers
    def __init__(self, max_passengers):
        # Set the maximum number of passengers
        self.max_passengers = max_passengers
        # Initialize an empty list to store passengers
        self.passengers = []

    # Method to add a passenger to the bus
    def add_passenger(self, person):
        # Check if the number of passengers is less than the maximum allowed
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"Pasajero agregado: {person.name}")
        else:
            # If the bus is full, print a message
            print("El bus está lleno. No se pueden agregar más pasajeros.")

    # Method to remove a passenger from the bus
    def remove_passenger(self):
            # Check if there are passengers in the bus
            if self.passengers:
                # Remove the last passenger from the list
                person = self.passengers.pop()
                print(f"Pasajero bajó: {person.name}")
            else:
                # If there are no passengers, print a message
                print("No hay pasajeros en el bus")

# Create a class called "Person" to represent a passenger.
class Person:
    # Initialize the class with the name of the person
    def __init__(self, name):
        # Set the name of the person
        self.name = name

# Create an instance of the Bus class with a maximum of 3 passengers
bus = Bus(3)
# Create instances of the Person class
person1 = Person("Alice")
person2 = Person("Bob")
person3 = Person("Charlie")
person4 = Person("David")
# Add passengers to the bus
bus.add_passenger(person1)
bus.add_passenger(person2)
bus.add_passenger(person3)
bus.add_passenger(person4) 
# Remove passengers from the bus
bus.remove_passenger()
bus.remove_passenger()
bus.remove_passenger()
bus.remove_passenger() 


