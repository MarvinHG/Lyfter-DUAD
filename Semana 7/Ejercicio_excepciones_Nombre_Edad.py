'''
1. Cree un programa que:
- Pida al usuario su **nombre**
    - Si el nombre es numérico (`isdigit()`), **haga `raise ValueError("El nombre no puede ser un número")`**
    - Ejemplo:
        - Entrada:
            
            ```python
            "Ingrese su nombre: " 5
            ```
            
        - Salida:
            
            ```python
            "El nombre no puede ser un número"
            ```
            
- Luego pida su edad
    - Si no es un número válido, capture el `ValueError` y muestre un mensaje
    - Ejemplo:
        - Entrada:
            
            ```python
            "Ingrese su edad: " cinco
            ```
            
        - Salida:
            
            ```python
            "Número no valido"
            ```
            
- Si todo sale bien, imprima un mensaje: `"Hola <nombre>, su edad es <edad>"`
- Ejemplo:
    - Entrada:
        
        ```python
        "Ingrese su nombre: " "Jean Carlo"
        "Ingrese su edad: " 27
        ```
        
    - Salida:
        Hola Jean Carlo, su edad es 27
'''
# Function to get the user's name
def your_name():
    # Ask the user to enter their name
    name = input("Ingrese su nombre: ")
    # Validate that the name does not contain any numeric characters
    if any(char.isdigit() for char in name):
        # Raise an error if the name contains numbers
        raise ValueError("El nombre no puede ser un número")
    # Return the validated name
    return name


# Function to get the user's age
def your_age():
    # Ask the user to enter their age
    try:
        age = int(input("Ingrese su edad: "))
    except ValueError:
        # Raise a new error if the user did not enter a valid number
        raise ValueError("Número no valido")
    # Return the validated age
    return age


# Main Function
def main():
        # Loop until the user enters a valid name
        while True:
            try:
                name = your_name()
                break # Exit the loop if the name is valid
            except ValueError as ex:
                # Show the error and ask the user to try again
                print(f"{ex}. Por favor ingrese un nombre válido.\n")

        # Loop until the user enters a valid age
        while True:
            try:
                age = your_age()
                break # Exit the loop if the age is valid
            except ValueError as ex:
                # Show the error and ask the user to try again
                print(f"{ex}. Por favor ingrese una edad válida.\n")

        # Display the final message    
        print(f"Hola {name}, su edad es: {age}")

# Run program only if executed directly
if __name__ == '__main__':
	main()