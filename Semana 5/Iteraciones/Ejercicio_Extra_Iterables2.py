'''
1. **Cree un programa que verifique si todos los elementos de una lista son positivos**
- Restricciones:
    - No use funciones como `all()`
- Ejemplo:
    - Entrada:
        
        ```python
        my_list = [3, 6, 0, -2, 4]
        ```
        
    - Salida:
        "Hay al menos un número negativo o cero"
'''
# Ask the user how many numbers they want in the list
list_size = int(input("Ingrese de cuantos valores quiere que sea la lista: "))
# Create the list and the variable
counter = 0
my_list = []
#Create the loop
for index in range(list_size):
    num = int(input("Ingrese un numero: "))
    my_list.append(num)
    # Check if the number is zero or negative
    if  num <= 0:
        counter = counter +1

# If no negative or zero numbers were found, all numbers are positive
if counter <= 0:
    print("Todos los numeros de la lista son positivos")
else:
    print("Hay al menos hay un número negativo o cero en la lista")