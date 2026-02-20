# This module contains the main menu functions for the student management system.
from actions import is_valid_name, is_valid_section, student_exists, is_valid_grade, sort_students_by_average, get_student, delete_student, get_failed_students
from data import imported_students_from_csv , export_students_to_csv


# ========== Function to fill student information ========== 
def menu_1_fill_student_info(students):
    # Loop to allow adding multiple students
    while True:
        # Create a dictionary to store student information
        student = {}
        # Ask for student information

        # Loop to validate the student's name and section
        while True:
            # Get the full name of the student (with EOFError handling)
            try:
                full_name = input("Ingrese el nombre completo del estudiante: ")
            except EOFError:
                print("\nEntrada cancelada por el usuario.\n") 
                return # Exit the function if the user cancels the input and return to the main menu
            # Calling the function to validate the name
            if not is_valid_name(full_name): 
                print("\nNombre inválido. No debe estar vacío ni contener números.\n")
                continue

            # Get the section of the student
            section = input("Ingrese la sección del estudiante (ejemplo 10A): ")
            # Calling the function to validate the section
            if not is_valid_section(section): 
                print("\nSección inválida. Ejemplo válido: 10A, 11B.\n")
                continue

            # Calling the function to check if the student already exists
            if student_exists(students, full_name, section): 
                print("\nEl estudiante ya existe en esa sección.\n")
                continue

            # If all validations pass, save the student's name and section
            student["full_name"] = full_name.strip()
            student["section"] = section.upper()
            break
        
        # Get the grades for each subject and validate them
        subjects = [
            ("spanish_grade", "Español"),
            ("english_grade", "Inglés"),
            ("social_studies_grade", "Sociales"),
            ("science_grade", "Ciencias")
        ]
        # Loop through each subject to get and validate the grade
        for key, subject_name in subjects:
            while True:
                grade = input(f"Ingrese la nota de {subject_name}: ")

                if is_valid_grade(grade):
                    student[key] = float(grade)
                    break # Exit the loop if the grade is valid
                else:
                    print("\nNota inválida. Debe ser un número entre 0 y 100.\n")

        # Calculate average grade
        student["average"] = (
            student["spanish_grade"]
            + student["english_grade"]
            + student["social_studies_grade"]
            + student["science_grade"]
        ) / 4

        # Save student to the list
        students.append(student)

        print("\nEstudiante registrado correctamente.\n")

        # Ask if the user wants to add another student
        option = input("¿Desea agregar otro estudiante? (s/n): ").lower()

        if option not in ("s", "si", "sí"):
            # Return to main menu
            break
# End of function to fill student information


# ========== Function to show students information ========== 
def menu_2_view_all_students(students):
    if not students: # Check if there are no students registered
        print("\nNo hay estudiantes registrados actualmente.\n")
        return # Exit the function if there are no students to show

    print("\nListado de estudiantes registrados:\n")

    # Loop through the list of students and print their information
    for index, student in enumerate(students, start=1):
        print(f"Estudiante #{index}")
        print(f"Nombre Completo : {student['full_name']}")
        print(f"Sección         : {student['section']}")
        print(f"Nota Español    : {student['spanish_grade']}")
        print(f"Nota Inglés     : {student['english_grade']}")
        print(f"Nota Sociales   : {student['social_studies_grade']}")
        print(f"Nota Ciencias   : {student['science_grade']}")
        print("-" * 40)

    print()# Print an empty line for better formatting after listing all students
# End of function to show students information


# ========== Function to show the Top 3 average grades ========== 
def menu_3_top_3_students(students):
    # Check if there are no students registered
    if not students:
        print("\nNo hay estudiantes registrados para mostrar.\n")
        return

    # Get ordered students from actions
    ordered_students = sort_students_by_average(students)

    print("\n===== TOP 3 ESTUDIANTES =====")
    # Loop through the top 3 students and print their information
    for index, student in enumerate(ordered_students[:3], start=1):
        print(f"\n#{index}")
        print(f"Nombre: {student['full_name']}")
        print(f"Sección: {student['section']}")
        print(f"Promedio: {student['average']:.2f}")
# End of function to show the Top 3 average grades


# ========== Function to show the average grade among all students' grades ==========
def menu_4_average_grade(students):
    # Check if there are no students registered
    if not students: 
        print("\nNo hay estudiantes registrados para calcular el promedio.\n")
        return
    # Calculate the average of all students' averages
    total_average = sum(student["average"] for student in students)
    average_grade = total_average / len(students)
    print(f"\nEl promedio general entre todos los estudiantes es: {average_grade:.2f}")
# End of function to show the average grade among all students' grades


# ========== Function to export data to CSV ==========
def menu_5_export_data_to_csv(students):
    # Check if there are no students registered
    if not students:
        print("\nNo hay datos para exportar.\n")
        return
    # Call the function to export students to CSV and check if it was successful
    success = export_students_to_csv(students)
    # Print the result of the export operation
    if success:
        print("\nDatos exportados correctamente a students.csv\n")
    else:
        print("\nOcurrió un error al exportar los datos.\n")
# End of function to export data to CSV


# ========== Function to import data from CSV ==========
def menu_6_import_data_from_csv(students): 
    #   Call the function to import students from CSV and store the result in a variable
    imported_students = imported_students_from_csv() 

    # Check if the imported students data is None (which indicates an error or that the file does not exist)
    if imported_students is None:
        print("\nNo existe un archivo previamente exportado para importar.\n")
        return

    # Clear current data and load imported data
    students.clear()
    students.extend(imported_students)

    print("\nDatos importados correctamente desde students.csv\n")
# End of function to import data from CSV


# ========== Function to delete a student (to be implemented) ==========
def menu_7_delete_student(students):
    # Check if there are no students registered
    if not students:
        print("\nNo hay estudiantes registrados para eliminar.\n")
        return
    # Ask the user for the full name and section of the student to delete
    full_name = input("Ingrese el nombre completo del estudiante a eliminar: ").strip()
    section = input("Ingrese la sección del estudiante (ejemplo 10A): ").strip()
    # Validate the name and section inputs
    if not student_exists(students, full_name, section):
        print("\nEl estudiante no existe.\n")
        return
    # Get the student information to show it before confirming deletion
    student = get_student(students, full_name, section)

    print("\nEstudiante encontrado:")
    print(f"Nombre: {student['full_name']}")
    print(f"Sección: {student['section']}")

    # Ask for confirmation before deleting the student
    confirm = input("¿Está seguro de que desea eliminar este estudiante? (s/n): ").lower()
    # If the user does not confirm, cancel the deletion and return to the main menu
    if confirm not in ("s", "si", "sí"):
        print("\nEliminación cancelada.\n")
        return
    # If the user confirms, call the function to delete the student and print the result
    if delete_student(students, full_name, section):
        print("\nEstudiante eliminado correctamente\n")
# End of function to delete a student


# ========== Function to show failed students (to be implemented) ==========
def menu_8_show_failed_students(students):
    # Check if there are no students registered
    if not students:
        print("\nNo hay estudiantes registrados.\n")
        return
    # Call the function to get the list of failed students and store it in a variable
    failed_students = get_failed_students(students)
    # Check if there are no failed students and print a message if that's the case, then return to the main menu
    if not failed_students:
        print("\nNo hay estudiantes reprobados\n")
        return

    print("\n===== ESTUDIANTES REPROBADOS =====")
    # Loop through the list of failed students and print their information along with the subjects they failed
    for index, student in enumerate(failed_students, start=1):
        print(f"\n#{index}")
        print(f"Nombre: {student['full_name']}")
        print(f"Sección: {student['section']}")
        print("Materias reprobadas:")
        # Loop through the failed subjects of the student and print the subject name and grade
        for subject, grade in student["failed_subjects"].items():
            print(f" - {subject}: {grade}")
# End of function to show failed students


# ========== Menu Function ========== 
def menu(students):
    # Main menu loop (keeps running until the user chooses to exit)
    while True:
        print("\n===== SISTEMA DE GESTIÓN DE ESTUDIANTES =====")
        print("1. Ingresar la información del estudiante")
        print("2. Ver la información de todos los estudiantes")
        print("3. Ver el Top 3 de los estudiantes con mejor nota promedio")
        print("4. Ver la nota promedio entre las notas de todos los estudiantes")
        print("5. Exportar los datos")
        print("6. Importar los datos")
        print("7. Eliminar estudiante")
        print("8. Mostrar estudiantes reprobados")
        print("9. Salir")

        # Ask the user to select an option
        option  = input("Seleccione una opción: ")
        if option  == "1":
            # Call the function to fill student information
            menu_1_fill_student_info(students)
        elif option  == "2":
            # Call the function to show student information
            menu_2_view_all_students(students)
        elif option  == "3":
            # Call the function to show the Top 3 average grades
            menu_3_top_3_students(students)
        elif option  == "4":
            # Call the function to show the average grade among all students' grades
            menu_4_average_grade(students)
        elif option  == "5":
            # Call the function to export data to CSV
            menu_5_export_data_to_csv(students)
        elif option  == "6":
            # Call the function to import data from CSV
            menu_6_import_data_from_csv(students)
        elif option  == "7":
            # Call the function to delete a student
            menu_7_delete_student(students)
        elif option  == "8":
            # Call the function to show failed students
            menu_8_show_failed_students(students)
        elif option  == "9":
            # Exit the program
            print("Saliendo del sistema...")
            break
        else:
            # Invalid option handling
            print("Opción inválida. Intente de nuevo.")
