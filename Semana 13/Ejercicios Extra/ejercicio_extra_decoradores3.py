'''
Ejercicios Extra de Decoradores 3

Cree una función que se llame multiply, la cual obtiene dos valores y los multiplica entre si
A esta función se le debe combinar dos decoradores:
@log_call: imprime el nombre de la función, los argumentos, fecha actual y el retorno
@validate_numbers: revisa que todos los argumentos sean numéricos
Ejemplo:
    Entrada:
        multiply(3, 4)
    Salida:
        "func:multiply - args: 3, 4 - [2025-07-17 14:00:00.000000] - Resultado: 12"
        "Resultado 12"
'''
from datetime import datetime

# Decorator that logs information
def log_call(func):
    # Wrapper function that logs information about the function call
    def wrapper(*args):
        # Get the current date and time
        today = datetime.today()
        # Execute the original function and store its result
        result = func(*args)
        # Display the function name, arguments, timestamp, and returned result
        print(f"func:{(func.__name__)} - args: {args} - {today} - Resultado: {result}")
        # Return the original result
        return result
    return wrapper


# Decorator that validates args
def validate_numbers(func):
    # Wrapper function that validates numeric arguments
    def wrapper(*args):
        # Validate each received parameter
        for parameter in args:
            # Raise an exception if the parameter is not a number
            if not isinstance(parameter, (int, float)):
                raise TypeError("Deben de ingresarse numeros")
        # Execute the original function and store its result
        result = func(*args)
        # Print the returned result
        print (f"Resultado: {result}")
        # Return the original result
        return result
    return wrapper

# Call the decorators to run the function
@validate_numbers
@log_call
def multiply(num1, num2):
    # Multiply two numbers and return the result
    return num1 * num2

multiply(5,5)