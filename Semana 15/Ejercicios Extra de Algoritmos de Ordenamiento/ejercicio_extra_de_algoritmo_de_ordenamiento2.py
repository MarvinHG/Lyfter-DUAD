'''
Validación de entrada antes de ordenar
- Cree una función que reciba una lista y valide:
    - Que todos los elementos sean números
    - Que no esté vacía
    - Luego aplique bubble_sort si pasa las validaciones
    - Si hay error, debe lanzar un mensaje apropiado
Ejemplo:
- Entrada:
    validated_bubble_sort([5, "hola", 2])
- Salida: 
    "Error: La lista contiene elementos no numéricos"
'''

def bubble_sort(numbers):
    # Validate that the list is not empty
    if not numbers:
        print("Error: La lista está vacía")
        return

    # Assume the list is valid until we find an invalid element
    valid_numbers = True

    # Validate all elements
    for num in numbers:
        if not isinstance(num, (int, float)):
            valid_numbers = False
            print("Error: La lista contiene elementos no numéricos")
            break

    # Only sort if all elements are valid
    if valid_numbers:
        # Go through the list multiple times to move the largest elements to the end
        for pass_number in range(0, len(numbers)-1):
            # Track whether any elements were swapped during this pass
            swapped = False
            # Compare each element with the one next to it      
            for position in range(len(numbers)-1):
                # Get the current element and the following element
                currect_number = numbers[position]
                next_number = numbers[position+1]
        
                print(
                    f'-- Pasada {pass_number},{position}. '
                    f'Elemento actual: {currect_number}, '
                    f'Siguiente elemento: {next_number}'
                )
        
        
                # Swap the elements if they are in the wrong order
                if currect_number > next_number:
                    print('El elemento actual es mayor. Intercambiando posiciones...')
        
                    numbers[position] = next_number
                    numbers[position+1] = currect_number
        
                    swapped = True
        
        
            # Stop the algorithm if no swaps were made
            if not swapped:
                break
        # Return the sorted list
        return numbers

my_numbers = [15, 3, 9, 1, "12", 7, 5, 20, 8]

my_numbers = bubble_sort(my_numbers)

if my_numbers is not None:
    print('Lista ordenada:', my_numbers)
