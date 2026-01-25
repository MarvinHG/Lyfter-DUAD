'''
1. Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Borrar resultado
Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. 
El resultado debe pasar a ser el nuevo numero actual.
Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.
'''
# Sum Function
def add(a, b):
    return a + b # Returns the sum of a and b

# Substract Function
def subtract(a, b):
    return a - b # Returns the subtraction of b from a

# Multiply Function
def multiply(a, b):
    return a * b # Returns the multiplication of a and b

# Divide Function
def divide(a , b):
    if b == 0: # Division is invalid when the divisor (b) is zero
        raise ValueError("No se puede dividir entre 0.") # Raise an error to avoid invalid division
    return a / b # Returns the result of the division

# Function to safely request a number from the user
def new_number():
    # Uses try/except to catch invalid inputs
    try:
        value = float(input("Ingrese el número: "))
    except ValueError:
        raise ValueError("Error: número inválido.")
    return value

# Main Function
def main():
    current_number = 0.0 # Stores the current result of the calculator
    # Menu Loop
    while True:
        # Display calculator menu
        print("------- Calculadora -------")
        print(f"Numero Actual: {current_number}")
        print("1- Ingresar un numero")
        print("2- Sumar")
        print("3- Restar")
        print("4- Multiplicar")
        print("5- Dividir")
        print("6- Borrar")
        print("7- Salir")

        # Try to read user option as an integer
        try:
            option = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Opcion invalida, debes ingresar un numero.")
            continue # Go back to menu because input is not valid
        
        # Option selected
        if option == 1:
            try:
                current_number = new_number() # Replace current number
            except ValueError as ex:
                print(ex)

        elif option == 2:
            try:
                value = new_number()
                current_number = add(current_number, value) # Add current number
            except ValueError as ex:
                print(ex)

        elif option == 3:
            try:
                value = new_number()
                current_number = subtract(current_number, value) # Subtract current number
            except ValueError as ex:
                print(ex)

        elif option == 4:
            try:
                value = new_number()
                current_number = multiply(current_number, value) # Multiply current number
            except ValueError as ex:
                print(ex)

        elif option == 5:
            try:
                value = new_number()
                current_number = divide(current_number, value) # Divide current number
            except ValueError as ex:
                print(ex)

        elif option == 6:
            current_number = 0.0 # Reset to zero
            print("Resultado borrado. Ahora el número actual es 0.")
            continue # Restart menu

        elif option == 7:
            print("Saliendo...")
            break # Exit the loop and end program

        else:
            print("Error: opción inválida.")
            continue # Invalid menu option, restart menu

# Run program only if executed directly
if __name__ == '__main__':
	main()