'''
Ejercicios Extra de Análisis de Algoritmos# 2

Considere los siguientes dos algoritmos:

def linear_search(my_list, target):
    for item in my_list:
        if item == target:
            return True
    return False


def binary_search(my_list, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False    


Preguntas:
¿Cuál es la complejidad de cada algoritmo?
¿En qué condiciones conviene usar cada uno?
¿Qué pasa si la lista no está ordenada?

'''


def linear_search(my_list, target):
    for item in my_list:       # O(n)
        if item == target:     # O(1)
            return True        # O(1)
    return False               # O(1)


def binary_search(my_list, target):
    low = 0                       # O(1)
    high = len(my_list) - 1       # O(1)

    while low <= high:            # O(log n)
        mid = (low + high) // 2   # O(1)

        if my_list[mid] == target:    # O(1)
            return True               # O(1)
        elif my_list[mid] < target:   # O(1)
            low = mid + 1             # O(1)
        else:
            high = mid - 1            # O(1)

    return False                  # O(1)



# Lista de prueba
my_list = [2, 4, 6, 8, 10, 12, 14]
#my_list = [10, 25, 3, 2, 7, 19, 35]

# Número que queremos buscar
target = 10

# Test Linear search
print("Linear Search:", linear_search(my_list, target))

# Test binary search
print("Binary Search:", binary_search(my_list, target))

'''
Preguntas:
¿Cuál es la complejidad de cada algoritmo?
linear_search es O(n)
binary_search es O(log n)
¿En qué condiciones conviene usar cada uno?
Usaría la búsqueda lineal para listas pequeñas o desordenadas, especialmente si solo necesito hacer una búsqueda.
Usaría la búsqueda binaria para listas ordenadas y grandes, especialmente si voy a realizar muchas búsquedas.
¿Qué pasa si la lista no está ordenada?
La búsqueda lineal seguirá funcionando correctamente, porque simplemente compara cada elemento con el objetivo.
La búsqueda binaria, en cambio, puede devolver un resultado incorrecto, porque su lógica depende de que los elementos estén ordenados.
'''