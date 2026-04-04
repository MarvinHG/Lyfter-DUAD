# Create a Student class to represent a student and their information, 
# including methods to calculate the average grade and convert the student data to a dictionary format 
# for easier handling in CSV operations.
class Student:
    # Initialize the Student class with the student's full name, section, and grades for each subject.
    def __init__(self, full_name, section, spanish, english, social, science):
        self.full_name = full_name
        self.section = section
        self.spanish_grade = spanish
        self.english_grade = english
        self.social_studies_grade = social
        self.science_grade = science
        self.average = self.calculate_average()
    # Method to calculate the average grade for the student based on their grades in each subject.
    def calculate_average(self):
        return (
            self.spanish_grade +
            self.english_grade +
            self.social_studies_grade +
            self.science_grade
        ) / 4
    # Method to convert the student's information into a dictionary format, which is useful for exporting to CSV.
    def to_dict(self):
        return {
            "full_name": self.full_name,
            "section": self.section,
            "spanish_grade": self.spanish_grade,
            "english_grade": self.english_grade,
            "social_studies_grade": self.social_studies_grade,
            "science_grade": self.science_grade,
            "average": self.average
        }
        

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
        student.full_name.strip().lower() == full_name.strip().lower()
        and student.section.strip().upper() == section.strip().upper()
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
            f"Nombre Completo : {student.full_name}\n"
            f"Sección         : {student.section}\n"
            f"Nota Español    : {student.spanish_grade}\n"
            f"Nota Inglés     : {student.english_grade}\n"
            f"Nota Sociales   : {student.social_studies_grade}\n"
            f"Nota Ciencias   : {student.science_grade}\n"
            + "-" * 40 + "\n"
        )

    return output
# End of function to get all students formatted as a string


# ========== Function to sort students by average grade in descending order ==========
def sort_students_by_average(students):
    return sorted(
        students,
        key=lambda student: student.average,
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
            f"Nombre: {student.full_name}\n"
            f"Sección: {student.section}\n"
            f"Promedio: {student.average:.2f}\n"
        )
    return output 
# End of function to get the top 3 students formatted as a string


# ========== Function to calculate general average grade for all students ==========
def calculate_general_average(students):
    total = sum(student.average for student in students)
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
    failed_students = []
    # Loop through the students list and check if any student has a grade below 60 in any subject. 
    # If so, add their information and the failed subjects to the failed_students list.
    for student in students:
        failed_subjects = {}
        # Check each subject grade and add it to the failed_subjects dictionary if it's below 60
        if student.spanish_grade < 60:
            failed_subjects["Español"] = student.spanish_grade

        if student.english_grade < 60:
            failed_subjects["Inglés"] = student.english_grade

        if student.social_studies_grade < 60:
            failed_subjects["Sociales"] = student.social_studies_grade

        if student.science_grade < 60:
            failed_subjects["Ciencias"] = student.science_grade
        # If the student has any failed subjects, add their information and the failed subjects to the failed_students list
        if failed_subjects:
            failed_students.append({
                "full_name": student.full_name,
                "section": student.section,
                "failed_subjects": failed_subjects
            })

    return failed_students


# ========== Function to get failed students formatted as a string ==========
def get_failed_students_formatted(students):
    if not students:
        return "\nNo hay estudiantes registrados.\n"

    failed_students = get_failed_students(students)

    if not failed_students:
        return "\nNo hay estudiantes reprobados.\n"

    output = "\n===== ESTUDIANTES REPROBADOS =====\n"

    for index, student in enumerate(failed_students, start=1):
        output += (
            f"\n#{index}\n"
            f"Nombre: {student['full_name']}\n"
            f"Sección: {student['section']}\n"
            f"Materias reprobadas:\n"
        )

        for subject, grade in student["failed_subjects"].items():
            output += f" - {subject}: {grade}\n"

    return output
# End of function to get failed students formatted as a string