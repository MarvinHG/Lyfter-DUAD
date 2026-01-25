'''
4. **Tabla de multiplicar personalizada**
    - Pida al usuario un número del 1 al 10
    - Muestre su tabla de multiplicar del 1 al 12
'''
# Ask the user for a number between 1 and 10
num = int(input("Ingrese un número del 1 al 10: "))

# Validate input range
if num < 1 or num > 10:
    print("Número fuera de rango. Por favor ingrese un número entre 1 y 10.")
else:
    print(f"Tabla de multiplicar del {num}:")
    
    # Loop from 1 to 12 and display the multiplication table
    for i in range(1, 13):
        result = num * i
        print(f"{num} x {i} = {result}")