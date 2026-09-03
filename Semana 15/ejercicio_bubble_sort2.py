'''
Ejercicios de Algoritmos de Ordenamiento 2
Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero

'''

def bubble_sort(numbers):

    # Go through the list multiple times to move the smallest elements to the beginning
    for pass_number in range(0, len(numbers) - 1):

        # Track whether any elements were swapped during this pass
        swapped = False

        # Compare elements from right to left
        for position in range(len(numbers) - 1, pass_number, -1):

            # Get the current element and the previous element
            current_number = numbers[position]
            previous_number = numbers[position - 1]

            print(
                f'-- Pasada {pass_number}, posición {position}. '
                f'Elemento actual: {current_number}, '
                f'Elemento anterior: {previous_number}'
            )

            # Swap the elements if the previous element is greater
            if previous_number > current_number:

                print('El elemento anterior es mayor. Intercambiando posiciones...')

                numbers[position] = previous_number
                numbers[position - 1] = current_number

                swapped = True

        # Stop the algorithm if no swaps were made
        if not swapped:
            return

my_numbers = [15, 3, 9, 1, 12, 7, 5, 20, 8]

bubble_sort(my_numbers)

print('Lista ordenada:', my_numbers)