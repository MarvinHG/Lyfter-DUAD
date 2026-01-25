'''
2. Cree un programa que use una lista para eliminar keys de un diccionario.
    1. Ejemplos:
    2. `list_of_keys = [’access_level’, ‘age’]`
    `employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}`
    → `{’name’: ‘John’, 'email’: ‘john@ecorp.com’}`
'''
#Create a list of keys
list_of_keys =  ['access_level','age']
#Create the dictionary
employee = {
    'name':'John',
    'email':'john@ecorp.com',
    'access_level':5,
    'age':28
    }
# Loop through the list of keys 
for index in range(len(list_of_keys)):
    # If the key exists in the dictionary, remove it
    if list_of_keys[index] in employee:
        employee.pop(list_of_keys[index])
# Display the updated dictionary
print(employee)