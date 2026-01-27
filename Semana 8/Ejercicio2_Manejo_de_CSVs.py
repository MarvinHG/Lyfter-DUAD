'''
2. Lea sobre el resto de métodos del módulo `csv` y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por 
*tabulaciones* en vez de por *comas*.
    1. Ejemplo de archivo final:
        
        ```
        nombre	genero	desarrollador	clasificacion
        Grand Theft Auto IV	Accion	Rockstar Games	M
        The Elder Scrolls IV: Oblivion	RPG	Bethesda	M
        Tony Hawk's Pro Skater 2	Deportes	Activision	T
        ```
'''
from pathlib import Path # Used to handle file paths in a clean and cross-platform way
import csv # Module used to create, read, and manipulate CSV files

HEADERS = ["nombre", "genero", "desarrollador", "clasificacion"] # CSV column headers

# Function to write a CSV file
def write_csv_file(file_path, video_games):
    try:
        file_exists = file_path.exists() # Check if the CSV file already exists
        mode = "a" if file_exists else "w" # Append if it exists, otherwise create a new file

        with open(file_path, mode, newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file,delimiter="\t", fieldnames=HEADERS) # Create a CSV writer using dictionary keys separate them with tabs

            # Write headers only if the file does not exist
            if not file_exists:
                writer.writeheader()

            # Write Videogames Info
            for game in video_games:
                writer.writerow(game)

    except PermissionError:
        print("Permisos insuficientes para escribir el archivo.")

    except csv.Error as e:
        print(f"Error en el formato del archivo CSV: {e}")

    except KeyError as e:
        print(f"Falta un campo requerido en los datos: {e}")

    except IOError as e:
        print(f"Error de entrada/salida al escribir el archivo: {e}")


# Main Function
def main():
    base_path = Path(__file__).parent
    file_name = base_path / "videojuegos_con_tabs.csv"
    video_games = []

    # Validate the number of video games
    try:
        num = int(input("¿Cuántos videojuegos deseas ingresar?: "))
        if num <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
    except ValueError as e:
        print(f"Entrada inválida: {e}")
        return

    # Data entry
    for index in range(num):
        print(f"\nVideojuego #{index + 1}")

        name = input("Nombre: ").strip()
        genre = input("Género: ").strip()
        developer = input("Desarrollador: ").strip()
        classification = input("Clasificación ESRB: ").strip()

        if not all([name, genre, developer, classification]):
            print("Todos los campos son obligatorios.")
            return

        # Create the Dictionary
        video_games.append({
            "nombre": name,
            "genero": genre,
            "desarrollador": developer,
            "clasificacion": classification
        })

    # Call the function to Save the file as CSV
    write_csv_file(file_name, video_games)
    print("\n Los videojuegos se han guardado correctamente en 'videojuegos_con_tabs.csv'")

if __name__ == "__main__":
    main()