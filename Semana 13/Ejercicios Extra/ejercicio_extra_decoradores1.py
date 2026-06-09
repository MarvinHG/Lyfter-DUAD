'''
Ejercicios Extra de Decoradores 1

Cree una función que imprima “Hola, [nombre]” dos veces: 
Cree un decorador @repeat_twice que haga que la función decorada se ejecute dos veces seguidas, 
con los mismos argumentos 
Ejemplo: 
    Salida: 
        "Hola, Jeanca" 
        "Hola, Jeanca"

'''
# Decorator that prints the function twice
def repeat_twice(func):
    # Wrapper function that executes the original function twice
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

# Call the decorator to run the function
@repeat_twice
def greet(name):
    # Prints a greeting message
    print(f"Hola, {name}")


new_greet = greet("Marvin")