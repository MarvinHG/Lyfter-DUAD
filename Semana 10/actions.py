from data import students, subjects, passing_grade, csv_filename
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


# ========== Function to check if student already exists ==========
def student_exists(full_name, section):
    # Check if a student with the same name and section already exists
    for student in students:
        if (
            student["full_name"].lower() == full_name.lower()
            and student["section"].upper() == section.upper()
        ):
            return True

    return False
# End of function to check if student already exists


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


# ========== Function to sort students by average grade in descending order ==========
def sort_students_by_average(students_list):
    return sorted(
        students_list,
        key=lambda student: student["average"],
        reverse=True
    )
# End of function to sort students by average grade in descending order


# ========== Function to export students to CSV ==========
def export_students_to_csv(students_list, filename= csv_filename):
    # Get the base path of the current file and create the full file path for the CSV file
    base_path = Path(__file__).parent
    file_path = base_path / filename
    # Try to open the file and write the students data to it
    try:
        # Open the file in write mode with UTF-8 encoding and create a CSV DictWriter
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "full_name",
                    "section",
                    "spanish_grade",
                    "english_grade",
                    "social_studies_grade",
                    "science_grade",
                    "average"
                ]
            )
            # Write the header and the students data to the CSV file
            writer.writeheader()
            writer.writerows(students_list)
        # If the file is written successfully, return True
        return True
    # If there is an error during the file writing process, catch the exception and print an error message, then return False
    except Exception as error:
        print(f"Error al exportar el archivo: {error}")
        return False
# End of function to export students to CSV


# ========== Function to import students from CSV (to be implemented) ==========
def imported_students_from_csv(filename= csv_filename):
    # Get the base path of the current file and create the full file path for the CSV file
    base_path = Path(__file__).parent
    file_path = base_path / filename
    # Check if the file exists before trying to read it
    if not file_path.exists():
        return None
    # Create an empty list to store the imported students
    students_list = []
    # Try to open the file and read the students data from it
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            # Loop through each row in the CSV file and create a student dictionary, then add it to the students_list
            for row in reader:
                student = {
                    "full_name": row["full_name"],
                    "section": row["section"],
                    "spanish_grade": float(row["spanish_grade"]),
                    "english_grade": float(row["english_grade"]),
                    "social_studies_grade": float(row["social_studies_grade"]),
                    "science_grade": float(row["science_grade"]),
                    "average": float(row["average"])
                }
                # Add the student dictionary to the students_list
                students_list.append(student)
        # If the file is read successfully, return the list of students
        return students_list
    # If there is an error during the file reading process, catch the exception and print an error message, then return None
    except Exception as error:
        print(f"Error al importar el archivo: {error}")
        return None
# End of function to import students from CSV


# ========== Function to delete a student ==========
def delete_student(students_list, full_name, section):
    # Loop through the students list and remove the student that matches the given full name and section, 
    # then return True. If no matching student is found, return False.
    for student in students_list:
        if (
            student["full_name"].lower() == full_name.lower()
            and student["section"] == section.upper()
        ):
            students_list.remove(student)
            return True

    return False
# End of function to delete a student


# ========== Function to get a student ==========
def get_student(students_list, full_name, section):
    # Loop through the students list and return the student that matches 
    # the given full name and section.
    for student in students_list:
        if (
            student["full_name"].lower() == full_name.lower()
            and student["section"] == section.upper()
        ):
            return student

    return None
# End of function to get a student


# ========== Function to get failed students ==========
def get_failed_students(students_list):
    # Create an empty list to store the failed students
    failed_students = []
    # Loop through the students list and check if any of their grades are below the passing grade
    for student in students_list:
        failed_subjects = {}

        for key, subject_name in subjects.items():
            if student[key] < passing_grade:
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