'''
Cree una clase de User que:
* Tenga un atributo de date_of_birth.
* Tenga un property de age.
Luego cree un decorador para funciones que acepten un User como parámetro que se encargue de revisar si 
el User es mayor de edad y arroje una excepción de no ser así.

'''

from datetime import date

# Create the User class
class User:
    # Store the user's date of birth
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        # Get today's date
        today = date.today()
        # Calculate the user's age
        return(
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )
    

# Decorator that validates the user is an adult
def validate_age(func):
    # Wrapper function that performs age validation
    def wrapper(*args):
        # Get the user object from the function arguments
        user = args[0]
        # Raise an exception if the user is underage
        if user.age < 18:
            raise ValueError("El usuario debe ser mayor de edad")
        # Execute the original function
        return func(*args)
    return wrapper

# Call the decorator to run the function
@validate_age
def buy_beer(user):
    print(f"Compra permitida, el usuario tiene {user.age} años")


adult_user = User(date(1996, 12, 18))
buy_beer(adult_user)