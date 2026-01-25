'''
1. Cree un diagrama de flujo que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “*Correcto*”. 
Sino, mostrar “*incorrecto*”.
    1. *Ejemplos*:
        1. 23, 30, 768 → Correcto (hay un 30)
        2. 10, 15, 5 → Correcto (10 + 15 + 5 = 30)
        3. 35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30
'''

# Define variables and ask the user to enter three numbers
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercero numero: "))

# Check numbers
if num1 == 30 or num2 == 30 or num3 == 30:
    print("Correcto!")
elif num1 + num2 + num3 == 30:
    print("Correcto!")
else:
    print("Incorrecto!") 