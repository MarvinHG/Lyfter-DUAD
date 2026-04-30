'''
Ejercicio extra OOP 1:
Cree una clase de Rectangle que:
- Tenga atributos width y height
- Tenga un método get_area() que retorne el área
- Tenga un método get_perimeter() que retorne el perímetro
- Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado
'''

# Define the Rectangle class
class Rectangle :
    def __init__(self, width, height):
        if width < 0 or height < 0:
            # Raise an exception if any value is negative
            raise ValueError("Existe un valor negativo, los valores deben ser positivos.")
        self.width = width
        self.height = height

    # Method to calculate area
    def get_area(self):
        return self.width * self.height

    # Method to calculate perimeter
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    

# Ask user information
try:
    width = float(input("Ingrese el ancho del rectángulo: "))
    height = float(input("Ingrese la altura del rectángulo: "))
    rectangle = Rectangle(width, height)
    print(f"El área del rectángulo es: {rectangle.get_area()}")
    print(f"El perímetro del rectángulo es: {rectangle.get_perimeter()}")
except ValueError as e:
    print(f"Error: {e}")

