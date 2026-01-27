'''
3. Cree una función que retorne la suma de todos los números de una lista.
    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    2. [4, 6, 2, 29] → 41
'''
# This function returns the sum of all numbers in a list
def sum_list(numbers_list):
    total = 0  # Variable to accumulate the sum
    
    for number in numbers_list:
        total += number
    
    return total


# Provide the parameter
result = sum_list([4, 6, 2, 29])
# Show the result
print(result)
