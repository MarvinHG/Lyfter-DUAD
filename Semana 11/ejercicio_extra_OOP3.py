'''
Ejercicio extra OOP3
Cree una clase Product con:
- Nombre, precio y cantidad
- Cree una clase Inventory que:
    *Guarde productos en una lista
    *Tenga métodos para:
        +Agregar un producto
        +Mostrar todos los productos
        +Calcular el valor total del inventario
'''

# Define the Product class
class Product:
    def __init__(self, name, price, quantity):
        if price < 0 or quantity < 0:
            # Raise an exception if any value is negative
            raise ValueError("Existe un valor negativo, los valores deben ser positivos.")
        
        self.name = name
        self.price = price
        self.quantity = quantity   

# Define the Inventory class
class Inventory:
    # Initialize the inventory with an empty list of products
    def __init__(self):
        self.products = []

    # Method to add a product to the inventory
    def add_product(self, product):
        self.products.append(product)

    # Method to show all products in the inventory
    def show_products(self):
        for product in self.products:
            print(f"Producto: {product.name}, Precio: {product.price}, Cantidad: {product.quantity}")

    # Method to calculate the total value of the inventory
    def calculate_total_value_of_inventory(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total


# Create an instance of Inventory
product1 = Product("Mouse", 5000, 2)
product2 = Product("Teclado", 8000, 3)
inventory = Inventory()

# Add products to the inventory
inventory.add_product(product1)
inventory.add_product(product2) 

# Show all products in the inventory
inventory.show_products()
print(f"El valor total del inventario es: {inventory.calculate_total_value_of_inventory()}")

