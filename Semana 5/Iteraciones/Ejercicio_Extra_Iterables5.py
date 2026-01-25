'''
1. Cree un programa que le pida al usuario ingresar 5 palabras. 
Luego muestre una nueva lista con solo aquellas palabras que **tengan más de 4 letras**
- Ejemplo:
    - Entrada:
        
        ```python
        ['sol', 'estrella', 'luz', 'planeta', 'roca']
        ```
        
    - Salida:
        ['estrella', 'planeta']
'''
# Create two empty lists:
first_list = []
second_list = []
# Create the loop
for index in range(5):
    word = input("Ingrese una palabra: ")
    first_list.append(word)
    # If the word has more than 4 letters, add it to the second list
    if len(word) > 4:
        second_list.append(word) 
# Display the words that have more than 4 letters
print(f"De las palabras ingresadas, las que tienen mas de 4 letras son: {second_list}")