'''
Ejercicio Decoradores 1

Cree un decorador que haga print de los parámetros y retorno de la función que decore.
'''

# Decorator that prints the function parameters and return value
def decorador(func):
    # Wrapper function that intercepts the call
    def wrapper(*args):
        # Print the received parameters
        print(f"Parametros: {args}")
        # Execute the original function
        resultado = func(*args)
        # Print the returned value
        print(f"El resultado es: {resultado}")
        # Return the original result
        return resultado
    return wrapper

# Call the decorator to run the function
@decorador
def sum_numbers(num1, num2):
    return num1 + num2

new_sum = sum_numbers(5,5)