'''
3. Cree un diagrama de flujo que le pida un numero al usuario y muestre “*Fizz*” si es divisible entre 3, “*Buzz*” si es divisible entre 5, 
y “*FizzBuzz*” si es divisible entre ambos.
    1. *Ejemplos*:
        1. 33 → Fizz
        2. 25 → Buzz
        3. 30 → FizzBuzz
'''
# Ask the user to enter a number
num = int(input("Ingresa un numero: "))

# Check divisibility and display the appropriate result
if num % 5 == 0 and num % 3 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
else:
    print("El número no es divisible ni por 3 ni por 5")