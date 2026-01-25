'''
2. 5. Cree un diagrama de flujo que le pida 100 números al usuario y muestre el mayor de todos.
    1. *Ejemplos*:
        1. 4, 76, 43, 6, 8 → 76
'''
# Define variables
counter = 1
largest_number = 0

# Loop to collect 100 numbers
while counter <=100:
    num = int(input("Ingrese un numero: "))
    
    # On first iteration, set the initial largest number
    if counter == 1:
        largest_number = num
    # Compare and update if current number is greater
    elif num > largest_number:
        largest_number = num
    counter += 1  

# Display the largest number entered        
print(f"El numero mayor ingresado es: {largest_number} ")