'''
Ejercicios Extra de Análisis de Algoritmos #3

Analice la siguiente función:

def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1}-{key2}")


Preguntas:
¿Cuál es la complejidad temporal?
¿Cuanto dura si hay 1 millón de claves?
'''

def print_all_pairs(my_dict):
    for key1 in my_dict:          # O(n)
        for key2 in my_dict:      # O(n²)
            print(f"{key1}-{key2}")  # O(1)


'''
Preguntas:
¿Cuál es la complejidad temporal?
La complejidad es O(n^2) ya que hay 2 ciclos anidados
¿Cuanto dura si hay 1 millón de claves?
Tardaria muchisimo tiempo
'''