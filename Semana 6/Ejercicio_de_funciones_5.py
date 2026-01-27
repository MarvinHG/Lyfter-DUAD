'''
5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
'''
# Create a function to count the upper and lower cases of a string
def count_characters(word):
    upper = 0
    lower = 0

    for char in word:
        if char.isupper(): # Check if character is uppercase
            upper += 1
        elif char.islower(): # Check if character is lowercase
            lower +=1
    
    print(f"in {word} there is {upper} upper cases and {lower} lower cases")

count_characters("I love Nacion Sushi")