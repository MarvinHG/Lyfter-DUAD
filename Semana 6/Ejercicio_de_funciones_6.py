'''
6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
'''
# This function converts a string separated by dashes into a sorted string
def string_to_list(text):
    # Convert the string into a list
    word_list = text.split("-")

    # Sort the list alphabetically
    sorted_list = sorted(word_list)

    # Convert the list back into a string separated by dashes
    result = "-".join(sorted_list)

    print(result)

string_to_list("python-variable-funcion-computadora-monitor")