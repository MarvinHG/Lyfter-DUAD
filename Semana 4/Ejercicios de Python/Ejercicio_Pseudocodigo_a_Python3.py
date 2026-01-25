'''
3. Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado. 
Luego muestre el resultado de la suma.
    1. 5 → 15 (1 + 2 + 3 + 4 + 5)
    2. 3 → 6 (1 + 2 + 3)
    3. 12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)
'''

# Define variables
num = 0
counter = 1
total_sum = 0

# Ask the user to enter a number
num = int(input("Ingrese un numero: "))

# Loop from 1 to the entered number and accumulate the sum
while counter <= num:
    total_sum = total_sum + counter
    counter = counter + 1

# Display the result
print(f"La suma de los numeros desde el 1 hasta {num} es de : {total_sum}")