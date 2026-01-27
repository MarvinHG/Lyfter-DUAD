'''
4. Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas (`primero` y `segundo`) y 
los ordene de menor a mayor en dichas variables.
    1. Ejemplos:
        1. A: 56, B: 32 → A: 32, B: 56
        2. A: 24, B: 76 → A: 24, B: 76
        3. A: 45, B: 12 → A: 12, B: 45
'''

# Ask the user to enter two numbers
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

# Initialize variables to store the ordered values
first = 0
second = 0

# Compare and assign values in ascending order
if num1 <= num2:
    first = num1
    second = num2
else:
    first = num2
    second = num1

# Display the ordered result
print(f"Los numeros ordenados de menor a mayor son: A: {first}, B: {second}")