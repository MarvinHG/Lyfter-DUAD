'''
5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, 
seguido del numero ingresado más alto.
    1. Ejemplos:
    2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.
'''
#Create the list and variable
my_list = []
counter = 0
# Loop until the user has entered 10 numbers
while counter < 10:
    num = int(input("Ingrese un numero: "))
    my_list.append(num)
    counter = counter + 1
# Find the largest number in the list using the max() function
largest_number = max(my_list)
# Print the list and the largest number entered
print(f"{my_list}. El numero mas grande ingresado es: {largest_number}")