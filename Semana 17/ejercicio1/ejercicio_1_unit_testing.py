'''
Ejercicios de Unit Testing 1
    Cree los siguientes unit tests para el algoritmo bubble_sort:
        Funciona con una lista pequeña.
        Funciona con una lista grande (de más de 100 elementos.)
        Funciona con una lista vacía.
        No funciona con parámetros que no sean una lista.
'''

def bubble_sort(numbers):

    # Validate that the parameter is a list
    if not isinstance(numbers, list):
        raise TypeError("The parameter must be a list")

    # Go through the list multiple times
    for pass_number in range(len(numbers) - 1):

        # Track whether any elements were swapped
        swapped = False

        # Compare adjacent elements
        for position in range(len(numbers) - 1):

            current_number = numbers[position]
            next_number = numbers[position + 1]

            # Swap if elements are in the wrong order
            if current_number > next_number:

                numbers[position] = next_number
                numbers[position + 1] = current_number

                swapped = True

        # Stop if no swaps were made
        if not swapped:
            break

