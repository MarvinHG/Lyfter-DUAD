'''
Ejercicio Decoradores 2

Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, 
y arroje una excepción de no ser así.
'''

# Decorator that validates all parameters are numeric
def validate_numbers(func):
    # Wrapper function that performs validation before execution
    def wrapper(*args):
        # Validate each received parameter
        for parameter in args:
            # Raise an exception if the parameter is not a number
            if not isinstance(parameter, (int, float)):
                raise TypeError("Deben de ingresarse numeros")
        # Print the received parameters
        print(f"Los parametros a sumar son: {args}")
        # Execute the original function
        resultado = func(*args)
        # Print the returned result
        print (f"El resultado de la suma es: {resultado}")
        # Return the original result
        return resultado
    return wrapper

# Call the decorator to run the function
@validate_numbers
def sum_numbers(num1, num2):
    return num1 + num2

new_sum = sum_numbers(5,52)