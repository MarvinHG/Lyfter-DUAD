'''
Cree un programa que le pida tres números al usuario y muestre el mayor.
'''
#Request user inputs
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

# Verify the highest value
if num1 > num2 and num1 > num3:
    highest = num1
elif num2 > num1 and num2 > num3:
    highest = num2
else:
    highest = num3

# Display the results
print(f"El numero mayor entre {num1}, {num2} y {num3} es {highest}")
