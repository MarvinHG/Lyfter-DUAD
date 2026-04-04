'''
Ejercicios de OOP #1
Cree una clase de Circle con:
Un atributo de radius (radio).
Un método de get_area que retorne su área.
'''

# Create a class called "Circle" to calculate the area of the circle.
class Circle:

    # Initialize the class with the radius of the circle
    def __init__(self, radius):
        # Set the radius of the circle
        self.radius = radius

    # Method to calculate the area of the circle
    def get_area(self):
        # Calculate the area using the formula A = πr^2
        return 3.14 * self.radius ** 2

# Get the radius of the circle from the user
radius = float(input("Ingrese el radio del círculo: "))
# Create an instance of the Circle class with the given radius
circle1 = Circle(radius)
# Print the area of the circle
print("El area del circulo es:", circle1.get_area())