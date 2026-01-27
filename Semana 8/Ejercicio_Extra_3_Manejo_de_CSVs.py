'''
3. Cree un programa que abra un archivo `.csv` con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
- Lea el archivo `.csv` con videojuegos
- Cuente cuántos videojuegos hay de **cada género**
- Muestre el resultado de forma ordenada
- Ejemplo:
    - Salida:
        
        ```
        Géneros encontrados:
        Acción: 5
        Aventura: 3
        Deportes: 4
        ...
        ```
'''

from pathlib import Path # Used to handle file paths in a clean and cross-platform way
import csv # Module used to create, read, and manipulate CSV files

# Function to Reads a CSV file and counts how many video games belong to each genre.
def read_csv_file(file_path):

    try:
        genre_count = {} # Dictionary to store genre counts

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)# Reads the CSV as a dictionary per row

            # Iterates over each row of the CSV file
            for row in reader:
                genre = row["genero"].strip()# Gets the genre value and removes extra spaces

                # Skips rows where the genre field is empty
                if not genre:
                    continue

                # Increases the count for the current genre
                genre_count[genre] = genre_count.get(genre, 0) + 1

    except PermissionError:
        # Handles cases where the program does not have permission to read the file
        print("Permisos insuficientes para leer el archivo.")

    except csv.Error as e:
        # Handles CSV format-related errors
        print(f"Error en el formato del archivo CSV: {e}")

    except KeyError as e:
        # Handles missing required fields in the CSV file
        print(f"Falta un campo requerido en los datos: {e}")
    
    # Returns the dictionary with genre counts
    return genre_count

# Main Function
def main():
    base_path = Path(__file__).parent # Gets the directory where the script is located
    file_name = base_path / "videojuegos.csv" # Builds the full path to the CSV file
    
    # Calls the function to read the CSV file and get genre counts file
    genre_count = read_csv_file(file_name)

    # Displays the results
    print("Géneros encontrados:")
    for genre, count in genre_count.items():
        print(f"{genre}: {count}")

# Entry point of the program
if __name__ == "__main__":
    main()