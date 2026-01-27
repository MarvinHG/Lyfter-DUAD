'''
Dada `n` cantidad de notas de un estudiante, calcular:
    1. Cuantas notas tiene aprobadas (mayor a 70).
    2. Cuantas notas tiene desaprobadas (menor a 70).
    3. El promedio de todas.
    4. El promedio de las aprobadas.
    5. El promedio de las desaprobadas.
'''
# Define variables
grade_counter = 1
current_grade = 0
passed_grades_count = 0
failed_grades_count = 0
average_passed_grades = 0
average_failed_grades = 0
overall_average_grades = 0

# Ask the user how many grades will be entered
total_grades = int(input("Ingrese la cantidad de notas: "))

# Loop through each grade entry
while (grade_counter <= total_grades):
    current_grade = int(input(f"Ingrese la nota numero: {grade_counter}: "))

    # Classify the grade as passed or failed and update counters and sums
    if current_grade < 70 :
        failed_grades_count = failed_grades_count + 1
        average_failed_grades = average_failed_grades + current_grade
    else:
        passed_grades_count = passed_grades_count + 1
        average_passed_grades = average_passed_grades + current_grade
        
    overall_average_grades = overall_average_grades + (current_grade / total_grades)
    grade_counter += 1
    
# Calculate average of failed grades (if any)
if failed_grades_count > 0:
    average_failed_grades = average_failed_grades / failed_grades_count
else:
    average_failed_grades = 0  #"There is not failed grades"

# Calculate average of passed grades (if any)
if passed_grades_count > 0:
    average_passed_grades = average_passed_grades / passed_grades_count
else:
    average_passed_grades = 0  # "There is not passed grades"

# Display results
print(f"El estudiante tiene esta cantidad de notas aprobadas: {passed_grades_count}")
print(f"Este es el promedio de notas aprobadas: {average_passed_grades}")
print(f"El estudiante tiene esta cantidad de notas desaprobadas: {failed_grades_count}")
print(f"Este es el promedio de notas desaprobadas: {average_failed_grades}")
print(f"Este es el promedio total de notas: {overall_average_grades}")
