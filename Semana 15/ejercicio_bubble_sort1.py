'''
Ejercicios de Algoritmos de Ordenamiento 1
Crea un bubble_sort por tu cuenta sin revisar el código de la lección.
'''
def bubble_sort(numbers):
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
            return

my_numbers = [15, 3, 9, 1, 12, 7, 5, 20, 8]

bubble_sort(my_numbers)

print('lista ordenada', my_numbers)