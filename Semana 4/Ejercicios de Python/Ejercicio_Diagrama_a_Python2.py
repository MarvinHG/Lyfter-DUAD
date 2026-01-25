'''
2. Cree un diagrama de flujo que le pida 5 números al usuario y muestre el mayor.
    1. *Ejemplos*:
        1. 4, 76, 43, 6, 8 → 76
        2. 1, 2, 3, 6, 7 → 7
        3. 2132, 4355, 1132, 2323, 1214 → 4355
'''
# Define variables
counter = 1
largest_number = 0

while counter <=5:
    num = int(input("Ingrese un numero: "))
    
    # On first iteration, set the initial largest number
    if counter == 1:
        largest_number = num
    # Compare and update if current number is greater
    elif num > largest_number:
        largest_number = num
    counter += 1  # Increment loop counter

# Display the largest number entered        
print(f"El numero mayor ingresado es: {largest_number} ")