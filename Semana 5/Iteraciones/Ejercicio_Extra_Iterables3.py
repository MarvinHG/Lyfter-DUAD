'''
**Cree un programa que muestre el valor más pequeño de una lista sin usar `min()`.**
- Use una variable para comparar uno a uno
- Ejemplo:
    - Entrada:
        
        ```python
        my_list = [9, 4, 7, 1, 5]
        ```
        
    - Salida:
        
        ```python
        "El menor valor es 1"
        ```
        
'''
# Ask the user how many numbers they want in the list
list_size = int(input("Ingrese de cuantos valores quiere que sea la lista: "))
# Create the list and variable
smallest_number = 0
my_list = []
#Create the loop
for index in range(list_size):
    num = int(input("Ingrese un numero: "))
    my_list.append(num)
    # If this is the first iteration, set smallest_number to the first number
    if index == 0:
        smallest_number = num
    #compare the current number with the smallest
    elif num < smallest_number:
        smallest_number = num
# Print the smallest number found and the full list
print(f"el menor valor de la lista: {my_list}, es: {smallest_number}")