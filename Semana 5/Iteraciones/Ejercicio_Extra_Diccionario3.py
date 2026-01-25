'''
1. Dada una lista de productos vendidos, donde cada uno tiene categoría y precio, cree un diccionario que acumule el total por categoría.
- Ejemplo:
    - Entrada:
    products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]
'''

#List of products
products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]
# Create an empty dictionary
grouped_by_category= {}

# Loop through each product
for product in products:
    #Access the category from the current product
    category = product['category']
    price = product['price']
    # If the category doesn't exist yet in the dictionary, initialize it with 0
    if category not in grouped_by_category:
        grouped_by_category[category] = 0
    # Add the product's price to the total for its category
    grouped_by_category[category] += price
# Display the total sales per category
print(grouped_by_category)

