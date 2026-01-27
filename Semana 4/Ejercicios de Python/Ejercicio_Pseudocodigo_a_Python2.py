'''
Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos. 
Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”. 
Si es exactamente igual, muestre “Igual”.
'''
#Define variables

time_in_seconds = 0
difference = 0
result = ""

# Ask the user to input a time in seconds
time_in_seconds = int(input("ingrese un tiempo en segundos para ver si es mayor, menor o igual a 10 min: "))

difference = 600 - time_in_seconds

# Evaluate the result based on the difference
if difference == 0 :
    result = "Igual"
    print(f"El tiempo ingresado con respecto a 10 min en segundos es: {result}")
elif difference < 0:
    result = "Mayor"
    print(f"El tiempo ingresado con respecto a 10 min en segundos es: {result}")
else:
    print(f"Faltan: {difference} segundos para llegar a 10 minutos")