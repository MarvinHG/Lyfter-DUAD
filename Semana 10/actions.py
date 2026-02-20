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
def student_exists(students,full_name, section):
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
def sort_students_by_average(students):
    return sorted(
        students,
        key=lambda student: student["average"],
        reverse=True
    )
# End of function to sort students by average grade in descending order


# ========== Function to delete a student ==========
def delete_student(students, full_name, section):
    # Loop through the students list and remove the student that matches the given full name and section, 
    # then return True. If no matching student is found, return False.
    for student in students:
        if (
            student["full_name"].lower() == full_name.lower()
            and student["section"] == section.upper()
        ):
            students.remove(student)
            return True

    return False
# End of function to delete a student


# ========== Function to get a student ==========
def get_student(students, full_name, section):
    # Loop through the students list and return the student that matches 
    # the given full name and section.
    for student in students:
        if (
            student["full_name"].lower() == full_name.lower()
            and student["section"] == section.upper()
        ):
            return student

    return None
# End of function to get a student


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
            if student[key] < 65:
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