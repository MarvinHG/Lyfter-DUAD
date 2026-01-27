'''
Cree una función que reciba un string y retorne cuántas vocales contiene
Ejemplo:
Entrada:
"Hola mundo"

Salida:
4
'''
# Create a function to count valows in a string
def count_vowels(texto):
    vowels = "aeiou"
    count = 0
    #loop to find vowels
    for letra in texto.lower():
        if letra in vowels:
            count += 1
    print(f"Hay {count} vocales, en el texto")

count_vowels("Hola mundo")