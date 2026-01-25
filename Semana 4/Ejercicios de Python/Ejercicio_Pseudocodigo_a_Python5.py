'''
5. Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s. Recuerda que `1 km == 1000m` y `1 hora == 60 minutos * 60 segundos`.
    1. *Ejemplos*:
        1. 73 → 20.27
        2. 50 → 13.88
        3. 120 → 33.33
'''
# Define variables and get user input
kilometers_per_hour = int(input("Ingrese una velocidad en km/h: "))
meters_per_second = kilometers_per_hour * (5/18) # Convert speed to meters per second using the standard formula

#Display results
print(f"La velocidad ingresada en metros por segundos seria: {round(meters_per_second)}")


