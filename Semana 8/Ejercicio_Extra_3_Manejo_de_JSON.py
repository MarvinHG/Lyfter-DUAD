'''
3. Cree un programa que abra un archivo `.json` con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
- Lea el archivo JSON de Pokémon
- Para cada Pokémon, muestre sus **estadísticas principales** (por ejemplo: `ataque`, `defensa`, `velocidad`, etc.)
- Ejemplo:
    - Salida:
        
        ```
        Nombre: Pikachu
        Ataque: 55
        Defensa: 40
        Velocidad: 90
        
        Nombre: Bulbasaur
        Ataque: 49
        Defensa: 49
        Velocidad: 45
        ...
        ```
'''

from pathlib import Path # Used to handle file paths in a clean and cross-platform way
import json              # Used to work with JSON files


# Function to read a JSON file and display Pokémon information
def read_json_file(file_path):
    try:
        # Open the JSON file in read mode with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            # Convert JSON content into a Python list of dictionaries
            pokemons = json.load(file)

        # Iterate over each Pokémon in the list
        for pokemon in pokemons:
            # If the key does not exist, use "Desconocido" as default
            name = pokemon.get("name", {}).get("english", "Desconocido")
            attack = pokemon.get("base", {}).get("Attack", "Desconocido")
            defense = pokemon.get("base", {}).get("Defense", "Desconocido")
            speed = pokemon.get("base", {}).get("Speed", "Desconocido")

            # Display Pokémon information in a readable format
            print(f"Nombre: {name}")
            print(f"Ataque: {attack}")
            print(f"Defensa: {defense}")
            print(f"Velocidad: {speed}")
            print("-" * 30)

    # Handles the case where the JSON file does not exist
    except FileNotFoundError:
        print("Error: El archivo JSON no existe.")

    # Handles the case where the program does not have permission to read the file
    except PermissionError:
        print("Error: No tienes permisos para leer el archivo.")

    # Handles invalid or corrupted JSON format
    except json.JSONDecodeError:
        print("Error: El archivo JSON tiene un formato inválido.")



# Main function that controls the program flow
def main():
    base_path = Path(__file__).parent # Gets the directory where the script is located
    file_name = base_path / "pokemon.json" # Builds the full path to the CSV file
    
    # Read and display Pokémon data from the JSON file
    read_json_file(file_name)


# Program entry point
if __name__ == "__main__":
    main()