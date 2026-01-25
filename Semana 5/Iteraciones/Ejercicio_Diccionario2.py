'''
1. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
    1. Ejemplos:
    2. `list_a = [’first_name’, ‘last_name’, ‘role’]`
    `list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]`
    → `{’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}`
'''
# Create an empty dictionary to store the result
user_info = {}
# Create the list
list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']

# Create the loop
for index in range(len(list_a)):
    # Assign each key from list_a to the corresponding value from list_b
    user_info[list_a[index]] = list_b[index]

# Print the final dictionary
print(user_info)