'''
Ejercicios Extra de Decoradores 2

Cree un decorador @requires_login que:
Verifique si la variable global user_logged_in es True
Si no lo es, debe lanzar una excepción "Usuario no autenticado"
Si lo es, la función decorada se ejecuta normalmente
Ejemplo:
    Entrada:
        user_logged_in = False

        @requires_login
        def view_profile():
            print("Mostrando perfil del usuario")
'''
# Decorator that checks if the user is authenticated
def requires_login(func):
    # Wrapper function that checks if the user is authenticated
    def wrapper(*args, **kwargs):
        # Raise an exception if the user is not logged in
        if not user_logged_in:
            raise Exception("Usuario no autenticado")
        # Execute the original function if authentication succeeds
        return func(*args, **kwargs)
    return wrapper


# Global variable that represents the authentication status
user_logged_in = True

# Call the decorator to run the function
@requires_login
def view_profile():
    # Display the user's profile information
    print("Mostrando perfil del usuario")

view_profile()