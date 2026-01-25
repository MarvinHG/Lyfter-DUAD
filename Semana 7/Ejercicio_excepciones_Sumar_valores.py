'''
1. Cree una función `sumar_valores(lista)` que:
- Reciba una lista de elementos (strings, enteros, flotantes mezclados)
- Intente convertir cada elemento a tipo `float`
- Si puede, sume el valor y muestre: `"<valor> sumado correctamente"`
- Si no puede, muestre: `"Elemento inválido: <valor>"`
- Al final, imprima la suma total
- Ejemplo:
    - Entrada:
        
        ```python
        my_list = ['10', 'manzana', '5.5', '3', 'n/a']
        ```
        
    - Salida:
        10.0 "sumado correctamente"
        "Elemento inválido: manzana"
        5.5 "sumado correctamente"
        3.0 "sumado correctamente"
        "Elemento inválido: n/a"
        "Total de la suma:" 18.5
'''
# Function to sum numeric values in a mixed list
def sum_values(values_list):

    total = 0 # Accumulates the sum of valid numeric values

    for num in values_list: # Loop through each element in the list
        try:
            number = float(num) # Attempt to convert the element to float
            total = total + number # Add converted number to total
            print(f"{number} sumado correctamente") # Success message
        except ValueError:
            # This executes if the element cannot be converted to float
            print(f"Elemento invalido: {num}")    
    print(f"Total de la suma: {total}") # Final total


# Main function to execute the program
def main():
    my_list = ['10', 'manzana', '5.5', '3', 'n/a'] # Example list with mixed values
    sum_values(my_list) # Call the sum function


# Run the program only if the file is executed directly
if __name__ == '__main__':
    main()