'''
Cree un programa que le pida al usuario su nombre, apellido, y age, y muestre 
si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
'''

# Request user input
name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))
full_info = ""

# Perform calculations
if(age < 4):
    full_info = "bebé"
elif(age < 10 ):
    full_info = "niño"
elif(age < 13 ):
    full_info = "preadolescente"
elif(age < 18 ):
    full_info = "adolescente"
elif(age < 30):
    full_info = "adulto joven"
elif (age < 60):
    full_info = "adulto"
else:
    full_info = "adulto mayor"

# Display the results
print(f"Hola {name} {last_name}, usted es un {full_info}.")