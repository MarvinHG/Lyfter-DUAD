'''
7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
    2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
    3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). 
    Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*
'''
# Function to check if a number is prime
def prime_number(n):
        # Numbers <= 1 are not prime
    if n <= 1:
        return False
    # 2 is prime
    if n == 2:
        return True
    # Any even number > 2 is not prime
    if n % 2 == 0:
        return False
    # Check divisors only up to the square root using n**0.5
    limit = int(n**0.5) + 1
    # Test only odd numbers
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

# Function to create a list just with prime number
def prime_list(number_list):
    # Create the new list
    final_list = []
    #Loop for any number on the list
    for num in number_list:
        #Calling the function to check if the number is prime
        check_prime = prime_number(num)
        if check_prime == True:
            final_list.append(num) #add just the prime number to the list
    print(final_list)

prime_list([1, 4, 6, 7, 13, 9, 67])
