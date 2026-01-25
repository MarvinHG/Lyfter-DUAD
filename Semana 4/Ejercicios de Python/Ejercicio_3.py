'''
3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
    1. Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.
'''
# Import the "random" library or module
import random
guessed = False
numero_random = random.randint(1, 10) # Generate a random number from 1 to 10

# Check if the number was guessed correctly
while guessed == False:
    guess_the_number = int(input("Intenta adivinar el numero generado aleatoriamente de 1 a 10: "))

    if (numero_random == guess_the_number):
        guessed = True
        print("¡Felicidades! Adivinaste el número.")
    else:
        print("No adivinaste, intenta otra vez.")
