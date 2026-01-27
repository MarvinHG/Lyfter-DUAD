'''
💡 **Ejercicios Extra de Manejo de CSVs**

1. Cree un programa que abra un archivo `.csv` con la información de videojuegos (el que fue generado en el ejercicio 1) y:
- Lea cada línea usando `csv.reader()`
- Muestre el contenido en pantalla de forma legible, línea por línea
- Ejemplo:
    - Salida:
        
        ```
        Nombre: Grand Theft Auto IV
        Género: Accion
        Desarrollador: Rockstar Games
        Clasificación: M
        ```      
'''

from pathlib import Path # Used to handle file paths in a clean and cross-platform way
import csv # Module used to create, read, and manipulate CSV files

# Function to read a CSV file
def read_csv_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file) # Creates a DictReader to read each CSV row as a dictionary
            for row in reader:# Iterates over each row in the CSV file
                print(f"Nombre: {row['nombre']}")# Displays the game name
                print(f"Género: {row['genero']}")# Displays the game genre
                print(f"Desarrollador: {row['desarrollador']}")# Displays the game developer
                print(f"Clasificación: {row['clasificacion']}")# Displays the game ESRB classification
                print("-" * 30) # Print a separation

    except PermissionError:
        print("Permisos insuficientes para leer el archivo.")

    except csv.Error as e:
        print(f"Error en el formato del archivo CSV: {e}")

    except KeyError as e:
        print(f"Falta un campo requerido en los datos: {e}")

    except FileNotFoundError:
        print("El archivo CSV no existe.")

# Main Function
def main():
    base_path = Path(__file__).parent
    file_name = base_path / "videojuegos.csv"
    
    # Call the function to read the CSV file
    read_csv_file(file_name)


if __name__ == "__main__":
    main()