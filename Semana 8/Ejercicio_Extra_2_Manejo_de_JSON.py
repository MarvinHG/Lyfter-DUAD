'''
2. Cree un programa que abra un archivo `.json` con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y::
- Lea el archivo `JSON` de Pokémon
- Pida al usuario un tipo de Pokémon
- Muestre todos los Pokémon que sean de ese tipo
- Ejemplo:
    - Entrada:
        
        ```python
        "Ingrese el tipo de pokemon desea buscar(water,electric,fire,etc): " 
        "Fuego"
        ```
        
    - Salida:
        
        ```python
        "Los pokemos que existen de ese tipo son: "
        Charmander
        Growlithe
        Victini
        ```
        
'''

from pathlib import Path # Used to handle file paths in a clean and cross-platform way
import json              # Used to work with JSON files


# Function that reads a JSON file and displays Pokémon that match a given type
def read_json_file(file_path, find_type):
    try:
        found = False  # Flag to check if at least one Pokémon is found

        # Open the JSON file in read mode with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            # Convert JSON content into a Python list of dictionaries
            pokemons = json.load(file)

            # Normalize user input to match JSON format (e.g. "fire" → "Fire")
            pokemon_type = find_type.capitalize()

            # Iterate over each Pokémon in the list
            for pokemon in pokemons:
                # If the key does not exist, use "Desconocido" as default
                name = pokemon.get("name", {}).get("english", "Desconocido")
                # If the key does not exist, return an empty list
                types = pokemon.get("type", [])

                # Check if the Pokémon belongs to the requested type
                if pokemon_type in types:
                    # Print the header only once
                    if not found:
                        print("Los pokemos que existen de ese tipo son: ")
                    found = True
                    print(f"Nombre: {name}")

            # If no Pokémon were found, show a message
            if not found:
                print("No se encontraron pokémon de ese tipo.")


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

    # Ask the user for the Pokémon type to search
    find_type = input("Ingrese el tipo de pokemon desea buscar(water,electric,fire,etc): ")
    
    # Read and display Pokémon data from the JSON file
    read_json_file(file_name, find_type)


# Program entry point
if __name__ == "__main__":
    main()