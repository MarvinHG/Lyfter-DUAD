'''
1. **Cree un programa que cuente cuántas veces aparece un número específico en una lista. 
Pida al usuario una lista de números y otro número a buscar**
- Ejemplo:
    - Entrada:
        
        ```python
        my_list = [4, 2, 7, 2, 8, 2, 1]
        numero_a_buscar = 2
        ```
        
    - Salida
        "El número 2 aparece 3 veces"
'''
# Ask how many numbers will have the list
list_number = int(input("Ingrese de cuantos valores quiere que sea la lista: "))
# Ask the user for the number they want to search for in the list
find_number = int(input("Ingrese el numero a encontrar en la lista: "))
# Create the list and variable
counter = 0
my_list = []
# Create the loop
for index in range(list_number):
    num = int(input("Ingrese un numero: "))
    my_list.append(num)
    if find_number == num:
        counter = counter +1
# Display how many times the number was found and show the full list
print(f"El numero: {find_number} aparece {counter} veces en la lista {my_list}")