'''
1. Cree una función `convertir_a_entero(lista)` que:
- Reciba una lista de strings
- Intente convertir cada elemento a entero usando `int()`
- Use `try-except` para atrapar los errores `ValueError`
- Si algún elemento no puede convertirse, mostrar `"No se pudo convertir el elemento: <valor>"` y continuar con los demás
- Ejemplo:
    - Entrada:
        
        ```python
        my_list = ['4', 'hola', '10', '5.2']
        ```
        
    - Salida:
        
        ```python
        "Resultado:"
        "4" "convertido a" 4
        "No se pudo convertir el elemento: hola"
        "10" "convertido a" 10
        "No se pudo convertir el elemento: 5.2"
        ```
'''
# Function to convert each element in the list to an integer
def converto_to_int(num_list):
    for num in num_list: # Iterate through each element in the list
        try:
            number = int(num) # Attempt to convert element to integer
            print(f"'{num}' convertido a {number}") # Print conversion success
        except ValueError:
            print(f"No se pudo convertir el elemento: {num}") # This block runs if conversion fails


# Main Function
def main():
    my_list = ['4', 'hola', '10', '5.2'] # Example list with mixed values
    converto_to_int(my_list) # Call the conversion function


# Run the program only if the file is executed directly
if __name__ == '__main__':
    main()