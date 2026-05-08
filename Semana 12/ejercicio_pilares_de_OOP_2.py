'''
Ejercicios de Los 4 Pilares de OOP #2

Cree una clase abstracta de Shape que:
    -Tenga los métodos abstractos de calculate_perimeter y calculate_area.
    -Ahora cree las siguientes clases que hereden de Shape e implementen esos métodos: Circle, Square y Rectangle.
    -Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

'''
# import the ABC module to create an abstract class
from abc import ABC, abstractmethod

# Create the abstract Shape class
class Shape(ABC):
    # Define the abstract method for calculating the perimeter
    @abstractmethod
    def calculate_perimeter(self):
        pass

    # Define the abstract method for calculating the area
    @abstractmethod
    def calculate_area(self):
        pass

# Create the Circle class that inherits from Shape
class Circle(Shape):
    # Initialize the radius attribute
    def __init__(self, radius):
        self.radius = radius

    # Implement the method to calculate the perimeter of the circle
    def calculate_perimeter(self):
        return 2 * 3.1416 * self.radius

    # Implement the method to calculate the area of the circle
    def calculate_area(self):
        return 3.1416 * (self.radius ** 2)

# Create the Square class that inherits from Shape
class Square(Shape):
    # Initialize the side attribute 
    def __init__(self, side):
        self.side = side

    # Implement the method to calculate the perimeter of the square
    def calculate_perimeter(self):
        return 4 * self.side

    # Implement the method to calculate the area of the square
    def calculate_area(self):
        return self.side ** 2

# Create the Rectangle class that inherits from Shape
class Rectangle(Shape):
    # Initialize the height and width attributes
    def __init__(self, height, width):
        self.height = height
        self.width = width

    # Implement the method to calculate the perimeter of the rectangle
    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

    # Implement the method to calculate the area of the rectangle
    def calculate_area(self):
        return self.height * self.width

#Get the area and perimeter of each shape
circle = Circle(radius=5)
square = Square(side=4)
rectangle = Rectangle(height=6, width=3)

print(f"Círculo - Perímetro: {circle.calculate_perimeter()}, Área: {circle.calculate_area()}")
print(f"Cuadrado - Perímetro: {square.calculate_perimeter()}, Área: {square.calculate_area()}")
print(f"Rectángulo - Perímetro: {rectangle.calculate_perimeter()}, Área: {rectangle.calculate_area()}")