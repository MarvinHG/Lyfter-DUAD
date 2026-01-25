'''
4. Cree un programa que abra un archivo `.csv` con la información de videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
- Lea el archivo `.csv` con videojuegos
- Pida al usuario ingresar el nombre de un **desarrollador** (ej. `"Ubisoft"`)
- Muestre todos los videojuegos desarrollados por esa empresa en formato legible:
- Ejemplo:
    - Salida:
        
        ```
        Videojuegos desarrollados por Ubisoft:
        - Assassin's Creed II (Clasificación: M, Género: Aventura)
        - Rayman Legends (Clasificación: E, Género: Plataforma)
        ```
'''

from pathlib import Path # Used to handle file paths in a clean and cross-platform way
import csv # Module used to create, read, and manipulate CSV files

# Function to Searches for video games developed by a specific developer
def find_games_by_developer(file_path, find_developer):

    try:
        found = False  # Flag to check if any game matches the developer

        # Opens the CSV file in read mode using UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file) # Reads each row as a dictionary

            # Iterates over each row of the CSV file
            for row in reader:
                # Checks if the game's developer matches the one entered by the user
                # Comparison is case-insensitive and ignores extra spaces
                if row["desarrollador"].strip().lower() == find_developer.lower(): 

                    # If this is the first matching game found, print the header only once
                    if not found:
                        print(f"Los videojuegos que fueron hechos por {find_developer} son:\n")
                        found = True # Sets the flag to True to indicate that at least one match was found

                    # Displays the video game name, classification, and genre
                    print(f"- {row['nombre']} (Clasificación: {row['clasificacion']}, Género: {row['genero']})")

        # If no games were found
        if not found:
            print("No hay videojuegos realizados por ese desarrollador.")


    except PermissionError:
        # Handles cases where the program does not have permission to read the file
        print("Permisos insuficientes para leer el archivo.")

    except csv.Error as e:
        # Handles CSV format-related errors
        print(f"Error en el formato del archivo CSV: {e}")

    except KeyError as e:
        # Handles missing required fields in the CSV file
        print(f"Falta un campo requerido en los datos: {e}")

# Main Function
def main():
    base_path = Path(__file__).parent # Gets the directory where the script is located
    file_name = base_path / "videojuegos.csv" # Builds the full path to the CSV file

    # Asks the user to enter a developer name
    find_developer = input("¿De que desarrollador desea encontrar videojuegos?: ").strip()
    
    # Calls the function to search and display video games by developer
    find_games_by_developer(file_name, find_developer)

# Entry point of the program
if __name__ == "__main__":
    main()