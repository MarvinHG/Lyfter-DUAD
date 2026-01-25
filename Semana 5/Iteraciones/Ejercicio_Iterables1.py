'''
1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
    1. Ejemplos:
    2. `first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]`
    `second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’]` ->
    Hay casos
    en los
    que la
    iteracion por
    indice es
    muy util
'''
# Create the lists
first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos' , 'los', 'la', 'por', 'es', 'util']

# Make the loop
for i in range(len(first_list)):
    # Print each pair of words from both lists in the same position
    print(f"{first_list[i]} {second_list[i]}")