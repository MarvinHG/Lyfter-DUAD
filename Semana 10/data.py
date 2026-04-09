# Import the csv module to handle CSV file operations
import csv
# Import the Path class from the pathlib module to handle file paths
from pathlib import Path


# ========== Function to export students to CSV ==========
def export_students_to_csv(students_list, filename= "students.csv"):
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
def imported_students_from_csv(filename= "students.csv"):
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