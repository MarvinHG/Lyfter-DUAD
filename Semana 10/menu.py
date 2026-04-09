# This module contains the main menu functions for the student management system.
from actions import get_basic_student_info, get_student_grades, get_all_students_formatted, calculate_average, calculate_general_average, get_top_3_students_formatted, get_student, get_failed_students_formatted, delete_student
from data import imported_students_from_csv , export_students_to_csv


# ========== Function to fill student information ========== 
def menu_1_fill_student_info(students):

    while True:
        # Get basic student information from user input and validate it
        basic_info = get_basic_student_info(students)
        if basic_info is None:
            return
        # Get student grades from user input and validate them
        grades = get_student_grades()
        student = {**basic_info, **grades}
        # Calculate the average grade for the student and add it to the student dictionary
        student["average"] = calculate_average(student)
        # Add the student to the students list
        students.append(student)

        print("\nEstudiante registrado correctamente.\n")

        option = input("\n¿Desea agregar otro estudiante? (s/n): \n").lower()
        if option not in ("s", "si", "sí"):
            break
# End of function to fill student information


# ========== Function to show students information ========== 
def menu_2_view_all_students(students):
    # Call the function to get the formatted list of all students and store it in a variable(result)
    result = get_all_students_formatted(students)
    print(result)
# End of function to show students information


# ========== Function to show the Top 3 average grades ========== 
def menu_3_top_3_students(students):
    # Call the function to get the formatted list of the Top 3 students with the best average grade and store it in a variable(result)
    result = get_top_3_students_formatted(students)
    print(result)
# End of function to show the Top 3 average grades


# ========== Function to show the average grade among all students' grades ==========
def menu_4_average_grade(students):
    # Check if there are no students registered
    if not students:
        print("\nNo hay estudiantes registrados.\n")
        return
    # Call the function to calculate the general average grade for all students and store it in a variable(average_grade)
    average_grade = calculate_general_average(students)
    # Print the average grade with two decimal places
    print(f"\nEl promedio general es: {average_grade:.2f}")
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
    #  Call the function to import students from CSV and store the result in a variable
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
    # Check if there are no students registered before attempting to delete
    if not students:
        print("\nNo hay estudiantes registrados para eliminar.\n")
        return

    full_name = input("Ingrese el nombre completo: ").strip()
    section = input("Ingrese la sección: ").strip()
    # Call the function to get the student based on the full name and section
    student = get_student(students, full_name, section)

    if not student:
        print("\nEl estudiante no existe.\n")
        return

    print("\nEstudiante encontrado:")
    print(f"Nombre: {student['full_name']}")
    print(f"Sección: {student['section']}")
    # Ask for confirmation before deleting the student
    confirm = input("¿Seguro que desea eliminar? (s/n): ").lower()
    # If the user does not confirm with "s", "si", or "sí", cancel the deletion and return to the menu
    if confirm not in ("s", "si", "sí"):
        print("\nEliminación cancelada.\n")
        return
    # Call the function to delete the student and check if it was successful
    if delete_student(students, full_name, section):
        print("\nEstudiante eliminado correctamente.\n")
# End of function to delete a student


# ========== Function to show failed students (to be implemented) ==========
def menu_8_show_failed_students(students):
    # Call the function to get the formatted list of failed students and store it in a variable
    result = get_failed_students_formatted(students)
    print(result)
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
        print("9. Salir\n")

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
            print("\nOpción inválida. Intente de nuevo.\n")
