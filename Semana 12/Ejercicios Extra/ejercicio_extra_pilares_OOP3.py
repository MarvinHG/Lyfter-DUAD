'''
Ejercicios extra de Los 4 Pilares de OOP #3

Cree una clase base Vehicle con los atributos:
    _brand
    _year

Agregue un método get_info() que devuelva una descripción del vehículo.
Luego cree dos clases hijas:
    Car
    Motorcycle

Cada una debe agregar su propio atributo (por ejemplo, doors o type) y sobrescribir el método get_info() 
para incluir esta información adicional.
Ejemplo:
    Entrada:
        vehicle1 = Car("Toyota", 2020, 4)
        vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")

    Salida:
        print(vehicle1.get_info())  # Toyota (2020) - 4 puertas
        print(vehicle2.get_info())  # Yamaha (2022) - Tipo: Deportiva

'''
#Create the Vehicle class
class Vehicle:

    # Constructor for common vehicle attributes
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    # Returns basic vehicle information
    def get_info(self):
        return f"{self._brand} ({self._year})"

#Create the Car class
class Car(Vehicle):

    # Constructor for car attributes
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self._doors = doors

    # Returns car information including doors
    def get_info(self):
        return f"{self._brand} ({self._year}) - {self._doors} puertas"

#Create the Motorcycle class
class Motorcycle(Vehicle):

    # Constructor for motorcycle attributes
    def __init__(self, brand, year, vehicle_type):
        super().__init__(brand, year)
        self._vehicle_type = vehicle_type

    # Returns motorcycle information including type
    def get_info(self):
        return f"{self._brand} ({self._year}) - Tipo: {self._vehicle_type}"


# Creating test objects
vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")


# Testing output
print(vehicle1.get_info())  
print(vehicle2.get_info())  