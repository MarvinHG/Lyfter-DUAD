'''
Ejercicios de Unit Testing 1
    Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de funciones 
'''

'''
Ejercio de funciones #5 para prueba de unit testing
    Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
        “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
'''

# Create a function to count uppercase and lowercase characters
def count_characters(word):

    upper = 0
    lower = 0

    for char in word:

        if char.isupper():
            upper += 1

        elif char.islower():
            lower += 1

    return upper, lower

'''
Ejercio de funciones #6 para prueba de unit testing
Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
'''


# Function to convert a dash-separated string into an alphabetically sorted string
def string_to_list(text):

    # Convert the string into a list
    word_list = text.split("-")

    # Sort the list alphabetically
    sorted_list = sorted(word_list)

    # Convert the list back into a string
    result = "-".join(sorted_list)

    return result


'''
Ejercio de funciones #7 para prueba de unit testing
    Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
        1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
        2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
        3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). 
        Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*
'''


# Function to check if a number is prime
def prime_number(n):

    # Numbers <= 1 are not prime
    if n <= 1:
        return False

    # 2 is prime
    if n == 2:
        return True

    # Any even number > 2 is not prime
    if n % 2 == 0:
        return False

    # Check divisors only up to the square root
    limit = int(n**0.5) + 1

    # Test only odd numbers
    for i in range(3, limit, 2):
        if n % i == 0:
            return False

    return True


# Function to create a list with only prime numbers
def prime_list(number_list):

    # Create the new list
    final_list = []

    # Loop through the numbers in the list
    for num in number_list:

        # Check if the number is prime
        if prime_number(num):
            final_list.append(num)

    return final_list
