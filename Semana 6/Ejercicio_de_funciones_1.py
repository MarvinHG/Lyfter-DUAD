'''
Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
'''
# This function prints a greeting message
def first_function():
    message = "¡Hola desde la primera función!"
    print(message)

    # Calling the second function
    second_function()


# This function prints a farewell message
def second_function():
    second_message = "¡Adiós desde la segunda función!"
    print(second_message)


# Calling the first function
first_function()
