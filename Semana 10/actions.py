# Import the csv module to handle CSV file operations
import csv
# Import the Path class from the pathlib module to handle file paths
from pathlib import Path


# ========== Function to validate student name ==========
def is_valid_name(name):
    # Remove leading and trailing spaces
    name = name.strip()
    # Check if name is empty
    if name == "":
        return False
    # Check if name contains numbers
    for char in name:
        if char.isdigit():
            return False
    return True
# End of function to validate student name


# ========== Function to validate section format ==========
def is_valid_section(section):
    # Remove leading and trailing spaces
    section = section.strip()
    # Check if section is empty
    if section == "":
        return False
    # Section must have at least 2 characters
    if len(section) < 2:
        return False
    # Separate number and letter
    number_part = section[:-1]
    letter_part = section[-1]
    # Validate number and letter
    if not number_part.isdigit():
        return False
    if not letter_part.isalpha():
        return False
    return True
# End of function to validate section format


# ========== Helper function to compare students ==========
def matches_student(student, full_name, section):
    return (
        student["full_name"].strip().lower() == full_name.strip().lower()
        and student["section"].strip().upper() == section.strip().upper()
    )
# End of helper function


# ========== Function to check if student already exists ==========
def student_exists(students, full_name, section):
    # Loop through the students list and check if any student matches the given full name and section 
    # using the matches_student helper function. 
    for student in students:
        if matches_student(student, full_name, section):
            # If a match is found, return True. 
            return True
    # If no match is found after checking all students, return False.
    return False
# End of function


# ========== Function to validate grade input ==========
def is_valid_grade(grade):
    # Check if grade is a valid number between 0 and 100
    try:
        grade = float(grade)
    except ValueError:
        return False
    if grade < 0 or grade > 100:
        return False
    return True
# End of function to validate grade input


# ========== Function to calculate average grade for a student ==========
def calculate_average(student):
    grades = [
        student["spanish_grade"],
        student["english_grade"],
        student["social_studies_grade"],
        student["science_grade"]
    ]
    return sum(grades) / len(grades)
# End of function to calculate average grade for a student


# ========== Function to get basic student information from user input ==========
def get_basic_student_info(students):
    while True:
        # -------- NAME --------
        while True:
            try:
                full_name = input("\nIngrese el nombre completo del estudiante: ")
            except EOFError:
                print("\nEntrada cancelada.\n")
                return None
            # Validate the name input and prompt again if it's invalid
            if not is_valid_name(full_name):
                print("\nNombre inválido.\n")
                continue
            break
        # -------- SECTION --------
        while True:
            section = input("\nIngrese la sección (ejemplo 10A): ")
            # Validate the section input and prompt again if it's invalid
            if not is_valid_section(section):
                print("\nSección inválida.\n")
                continue
            break
        # -------- DUPLICATE VALIDATION --------
        # Check if the student already exists in the students list and prompt again if it does
        if student_exists(students, full_name, section):
            print("\nEl estudiante ya existe en esa sección.\n")
            continue 
        return {
            "full_name": full_name.strip(),
            "section": section.upper()
        }
# End of function to get basic student information from user input


# ========== Function to get student grades from user input ==========
def get_student_grades():
    student = {}
    subjects = [
        ("spanish_grade", "Español"),
        ("english_grade", "Inglés"),
        ("social_studies_grade", "Sociales"),
        ("science_grade", "Ciencias")
    ]
    for key, subject_name in subjects:
        while True:
            grade = input(f"\nIngrese la nota de {subject_name}: ")
            if is_valid_grade(grade):
                student[key] = float(grade)
                break
            else:
                print("\nNota inválida.\n")
    return student
# End of function to get student grades from user input


# ========== Function to get all students formatted as a string ==========
def get_all_students_formatted(students):
    # Check if there are no students registered and return a message if that's the case
    if not students:
        return "\nNo hay estudiantes registrados actualmente.\n"

    output = "\nListado de estudiantes registrados:\n\n"
    # Loop through the list of students and format their information into a string for display
    for index, student in enumerate(students, start=1):
        output += (
            f"Estudiante #{index}\n"
            f"Nombre Completo : {student['full_name']}\n"
            f"Sección         : {student['section']}\n"
            f"Nota Español    : {student['spanish_grade']}\n"
            f"Nota Inglés     : {student['english_grade']}\n"
            f"Nota Sociales   : {student['social_studies_grade']}\n"
            f"Nota Ciencias   : {student['science_grade']}\n"
            + "-" * 40 + "\n"
        )

    return output
# End of function to get all students formatted as a string


# ========== Function to sort students by average grade in descending order ==========
def sort_students_by_average(students):
    return sorted(
        students,
        key=lambda student: student["average"],
        reverse=True
    )
# End of function to sort students by average grade in descending order


# ========== Function to get the top 3 students formatted as a string ==========
def get_top_3_students_formatted(students):
    # Check if there are no students registered and return a message if that's the case
    if not students:
        return "\nNo hay estudiantes registrados para mostrar.\n"
    # Sort the students by average grade in descending order and get the top 3 students
    ordered_students = sort_students_by_average(students)
    top_3 = ordered_students[:3]

    output = "\n===== TOP 3 ESTUDIANTES =====\n"

    for index, student in enumerate(top_3, start=1):
        output += (
            f"\n#{index}\n"
            f"Nombre: {student['full_name']}\n"
            f"Sección: {student['section']}\n"
            f"Promedio: {student['average']:.2f}\n"
        )
    return output 
# End of function to get the top 3 students formatted as a string


# ========== Function to calculate general average grade for all students ==========
def calculate_general_average(students):
    total = sum(student["average"] for student in students)
    return total / len(students)
# End of function to calculate general average grade for all students

# ========== Function to delete a student ==========
def delete_student(students, full_name, section):
    # Loop through the students list and delete the student that matches the given full name and section 
    # using the matches_student helper function.
    for index, student in enumerate(students):
        # If a match is found, delete the student from the list and return True.
        if matches_student(student, full_name, section):
            del students[index]
            return True
    # If no match is found after checking all students,
    return False
# End of function


# ========== Function to get a student ==========
def get_student(students, full_name, section):
    # Loop through the students list and return the student that matches the given full name and section
    for student in students:
        # If a match is found, return the student.
        if matches_student(student, full_name, section):
            return student
    # If no match is found after checking all students, return None.
    return None
# End of function


# ========== Function to get failed students ==========
def get_failed_students(students):
    # Create an empty list to store the failed students
    failed_students = []
    # Loop through the students list and check if any of their grades are below the passing grade
    for student in students:
        failed_subjects = {}
        # Dictionary to map the grade keys to their corresponding subject names
        subjects = {
            "spanish_grade": "Español",
            "english_grade": "Inglés",
            "social_studies_grade": "Sociales",
            "science_grade": "Ciencias"
        }
        for key, subject_name in subjects.items():
            if student[key] < 60:
                failed_subjects[subject_name] = student[key]
        # If the student has any failed subjects, add their information and the failed subjects to the failed_students list
        if failed_subjects:
            failed_students.append({
                "full_name": student["full_name"],
                "section": student["section"],
                "failed_subjects": failed_subjects
            })
    return failed_students
# End of function to get failed students


# ========== Function to get failed students formatted as a string ==========
def get_failed_students_formatted(students):
    # Check if there are no students registered
    if not students:
        return "\nNo hay estudiantes registrados.\n"
    # Call the function to get the list of failed students and store it in a variable
    failed_students = get_failed_students(students)
    # Check if there are no failed students and return a message if that's the case
    if not failed_students:
        return "\nNo hay estudiantes reprobados.\n"
    # Format the information of the failed students into a string for display
    output = "\n===== ESTUDIANTES REPROBADOS =====\n"
    # Loop through the list of failed students and add their information and the subjects they failed to the output string
    for index, student in enumerate(failed_students, start=1):
        output += (
            f"\n#{index}\n"
            f"Nombre: {student['full_name']}\n"
            f"Sección: {student['section']}\n"
            f"Materias reprobadas:\n"
        )
        # Loop through the failed subjects of the student and add them to the output string
        for subject, grade in student["failed_subjects"].items():
            output += f" - {subject}: {grade}\n"
    return output
# End of function to get failed students formatted as a string