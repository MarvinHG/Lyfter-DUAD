'''
Ejercicios Extra de Algoritmos de Ordenamiento 1
Modifique su implementación de bubble_sort para que:
- Cuente cuántas iteraciones (pasadas) realiza el algoritmo
- Cuente cuántos intercambios se hicieron en total
Ejemplo:
    Salida:
        Lista ordenada: [1, 2, 3, 4, 5]
        Iteraciones: 4
        Intercambios: 6
'''
def bubble_sort(numbers):
    # Counters for the total number of passes and swaps 
    iterations_count = 0 
    swap_count = 0

    # Go through the list multiple times to move the largest elements to the end
    for pass_number in range(0, len(numbers)-1):
        # Count each pass 
        iterations_count += 1
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

                # Count the swap 
                swap_count += 1

                swapped = True


        # Stop the algorithm if no swaps were made
        if not swapped:
            break
    # Return the sorted list and the counters 
    return numbers, iterations_count, swap_count

my_numbers = [15, 3, 9, 1, 12, 7, 5, 20, 8]

my_numbers, iterations_count, swap_count = bubble_sort(my_numbers)

print('Lista ordenada:', my_numbers)
print('Iteraciones:', iterations_count)
print('Intercambios:', swap_count)