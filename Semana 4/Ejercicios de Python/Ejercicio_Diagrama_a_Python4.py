'''
2. Cree un diagrama de flujo que le pida 100 números al usuario y muestre la suma de todos.
'''
# Define variables
counter = 1
total_sum = 0

# Loop to collect 100 numbers
while counter <=100:
    num = int(input("Ingrese un numero: "))
    total_sum = total_sum + num
    counter = counter + 1

# Display the total sum of the numbers entered        
print(f"La suma de todos los numeros ingresados es de: {total_sum} ")