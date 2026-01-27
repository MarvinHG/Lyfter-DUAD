'''
1. Cree un pseudocódigo que le pida un `precio de producto` al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
    1. Si el precio es menor a 100, el descuento es del 2%.
    2. Si el precio es mayor o igual a 100, el descuento es del 10%.
    3. *Ejemplos*:
        1. 120 → 108
        2. 40 → 39.2
'''
# Define Variables
product_price = 0
discount = 0
final_price = 0

# Ask the user to enter the product price
product_price = int(input("Ingrese el precio del producto: "))

# Apply discount based on price 
if product_price < 100:
    discount = product_price * 0.02
else:
    discount = product_price * 0.10

# Calculate the final price after discount
final_price = product_price - discount

# Display the results
print(f"El descuento de su compra es de: {discount}")
print(f"El precio final a pagar es de: {final_price}")