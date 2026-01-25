'''
Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras
Ejemplo:
Entrada:
["cielo", "sol", "maravilloso", "día"]
"Ingrese el numero de letras minimas en la palabra: " 4

Salida:
["cielo", "maravilloso"]
'''
# Crete a function to fliter words in a list
def filter_long_words(word_list):
    num = int(input("Ingrese el numero de letras minimas en la palabra: ")) #ask the user the number
    new_list = []
    #Loop to filter words 
    for word in word_list:
        if len(word) >= num:
            new_list.append(word)

    print(f"Las palabras que tiene mas de {num} letras son: {new_list}")
# calling the function
filter_long_words(["cielo", "sol", "maravilloso", "día"])  