'''
2. Cree un programa que abra un archivo `.csv` con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
- Lea el archivo CSV de videojuegos
- Pida al usuario una clasificación ESRB (por ejemplo: "T")
- Muestre todos los videojuegos que tengan esa clasificación
'''

from pathlib import Path # Used to handle file paths in a clean and cross-platform way
import csv # Module used to create, read, and manipulate CSV files

# Function to read a CSV file
def read_csv_file(file_path):
    find_classification = input("¿Qué clasificación desea encontrar en el archivo?: ").strip()

    try:
        found = False  # Flag to check if any game matches the classification

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Iterates over each row of the CSV file
            for row in reader:
                if row["clasificacion"] == find_classification: # Checks if the game's classification matches the one entered by the user
                    if not found:
                        # If this is the first matching game found,
                        # print the header only once
                        print("Los videojuegos que tienen esa clasificación son:\n")
                    found = True # Sets the flag to True to indicate that at least one match was found

                    print(f"Nombre: {row['nombre']}")# Displays the videogame name
                    print(f"Género: {row['genero']}")# Displays the videogame genre
                    print(f"Desarrollador: {row['desarrollador']}")# Displays the videogame developer
                    print(f"Clasificación: {row['clasificacion']}")# Displays the ESRB classification
                    print("-" * 30) # Display a separation

        # If no games were found
        if not found:
            print("No hay videojuegos con esa clasificación.")


    except PermissionError:
        print("Permisos insuficientes para leer el archivo.")

    except csv.Error as e:
        print(f"Error en el formato del archivo CSV: {e}")

    except KeyError as e:
        print(f"Falta un campo requerido en los datos: {e}")

# Main Function
def main():
    base_path = Path(__file__).parent
    file_name = base_path / "videojuegos.csv"
    
    # Call the function to read the CSV file
    read_csv_file(file_name)


if __name__ == "__main__":
    main()