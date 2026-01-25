'''
Cree un programa que reciba una lista de números y **calcule el promedio** de los valores,
luego cree una nueva lista con **solo los valores mayores al promedio**
- Ejemplo
    - Entrada
        
        ```python
        my_list = [10, 20, 30, 40, 50]
        ```
        
    - Salida:
        
        ```python
        "Promedio:" 30
        Nueva lista: [40, 50]
        ```
        

'''
# Ask the user how many numbers will be in the list
list_size = int(input("Ingrese de cuantos valores quiere que sea la lista: "))
# Create the lists and variables
first_list = []
total = 0
second_list = []
# Loop to collect the numbers from the user
for _ in range(list_size):
    num = int(input("Ingrese un número: "))
    first_list.append(num)
    total += num  # Add each number to the total sum
# Calculate the average of all numbers
average = total / len(first_list)
# Check which numbers are greater than the average
for num in first_list:
    if num > average:
        second_list.append(num)
# Show the average and the new list
print(f"El promedio de los números ingresados es: {average}")
print(f"Los valores mayores al promedio son: {second_list}")
