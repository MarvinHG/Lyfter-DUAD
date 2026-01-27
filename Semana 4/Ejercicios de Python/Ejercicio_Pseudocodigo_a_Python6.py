'''
6. Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, ingresando 1 si es mujer o 2 si es hombre, 
y muestre al final el porcentaje de mujeres y hombres.
    1. *Ejemplos*:
        1. 1, 1, 1, 2, 2, 2 → 50% mujeres y 50% hombres
        2. 1, 1, 2, 2, 2, 2 → 33.3% mujeres y 66.6% hombres
        3. 1, 1, 1, 1, 1, 2 → 83.3% mujeres y 16.6% hombres
'''

# Define variables
gender = 0
counter = 1
male_count = 0
female_count = 0
female_percentage = 0
male_percentage = 0

# Loop to collect gender input for 6 people
while counter <= 6:
    gender = int(input("ingrese 1 si es hombre o 2 si es mujer: "))
    counter = counter + 1
    if gender == 1:
        male_count = male_count + 1
    else:
        female_count = female_count +1
    
# Calculate percentages
female_percentage = round((female_count/6) * 100 , 2)
male_percentage = round((male_count/6) * 100 , 2) 

# Display results
print(f"El porcentaje de hombres ingresados es de: {male_percentage}")
print(f"El porcentaje de mujeres ingresados es de: {female_percentage}")