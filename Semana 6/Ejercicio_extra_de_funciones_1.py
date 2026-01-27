'''
Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto
Ejemplo:
Entrada:
"programacion"
"Ingrese el carácter que desea buscar:" "o"

Salida:
"Se a encontrado 2 veces el carácter"
'''
# Create a function to find a caracter on a string
def find_character():
    word = input("Ingresa una palabra o texto: ")
    character = input("Ingresa una letra, para saber cuantes veces aparece en el texto o palabra anteriormente ingresada: ")
    count = 0
    #loop trought  the word
    for char in word:
        if char == character:
            count +=1
    
    print(f"Se a encontrado {count} veces el caracter")

# Calling the function
find_character()
