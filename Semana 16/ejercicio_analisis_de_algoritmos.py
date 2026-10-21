'''
Ejercicios de Analisis de Algoritmos 1
Analice el algoritmo de bubble_sort usando la Big O Notation.
    - Todas las instrucciones del código son de tiempo constante, u O(1), siempre y cuando:
        - No sean ciclos ni recursividad.
        - No sean llamadas a funciones que no son de tiempo constante (que contienen ciclos o recursividad).
    - Los ciclos o recursividad son lo que puede cambiar ese tiempo:
        - O(1): cuando es un ciclo que siempre se ejecuta una cantidad de veces preestablecida. 
        Que no varia con su entrada.
        - O(n): cuando es un ciclo que va a ejecutarse siempre n cantidad de veces de acuerdo a su entrada.
        - O(n^2): cuando tenemos dos ciclos aninados.
            - La potencia va a subir dependiendo de la cantidad de ciclos anidados.
        - O(log n): cuando es un ciclo que va disminuyendo su cantidad de iteraciones cuanto mas grande sea el input.
'''
def bubble_sort(numbers):
    # Go through the list multiple times to move the largest elements to the end
    for pass_number in range(0, len(numbers)-1): # O(n)

        # Track whether any elements were swapped during this pass
        swapped = False # O(1)

        # Compare each element with the one next to it      
        for position in range(len(numbers)-1): # O(n^2)
            # Get the current element and the following element
            currect_number = numbers[position] # O(1)
            next_number = numbers[position+1] # O(1)

            print(
                f'-- Pasada {pass_number},{position}. '
                f'Elemento actual: {currect_number}, '
                f'Siguiente elemento: {next_number}'
            ) # O(1)

            # Swap the elements if they are in the wrong order
            if currect_number > next_number: # O(1)
                print('El elemento actual es mayor. Intercambiando posiciones...') # O(1)

                numbers[position] = next_number # O(1)
                numbers[position+1] = currect_number # O(1)

                swapped = True # O(1)

        # Stop the algorithm if no swaps were made
        if not swapped: # O(1)
            return # O(1)

my_numbers = [15, 3, 9, 1, 12, 7, 5, 20, 8] # O(1)

bubble_sort(my_numbers) # O(n^2) because the function is O(n^2)

print('lista ordenada', my_numbers) # O(1)