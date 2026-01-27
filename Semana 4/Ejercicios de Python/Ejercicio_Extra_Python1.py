'''
3. **Convertidor de unidades de temperatura**
    - Pida al usuario ingresar una temperatura en Celsius
    - Conviértala a Fahrenheit y Kelvin
    - Muestre los tres valores
'''
# Initialize variables
celsius = float(input("Ingrese la temperatura en °C: "))

# Convert to celsius and fahrenheit 
kelvin = celsius + 273.15
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C equivale a {kelvin}K y {fahrenheit}°F")
