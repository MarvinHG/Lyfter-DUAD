'''
Cree una función que le de la vuelta a un string y lo retorne.
    1. Esto ya lo hicimos en iterables.
    2. “Hola mundo” → “odnum aloH”
'''
# Create the function to return the reversed version of a string
def reverse_string(text):
    #Create the variable to store the reversed string
    reversed_text = ""

    # Loop through each character in the original string
    for char in text:
        reversed_text = char + reversed_text
    
    print(reversed_text)

reverse_string("hola mundo")

