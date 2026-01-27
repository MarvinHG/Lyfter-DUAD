'''
4. Cree un programa que abra un archivo `.json` con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
- Lea el archivo JSON
- Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
- Calcule y muestre el **promedio de nivel** para cada tipo:
- Ejemplo:
    - Salida:
    
    ```
    Tipo: Agua → Promedio de nivel: 42.6
    Tipo: Fuego → Promedio de nivel: 37.2
    Tipo: Planta → Promedio de nivel: 30.4
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

        # Dictionary to group levels by type
        type_levels = {}
        
        # Iterate over each Pokémon in the list
        for pokemon in pokemons:
            types = pokemon.get("type", [])
            level = pokemon.get("level")

            # Skip Pokémon that do not have a level or do not have any types defined
            if level is None or not types:
                continue

            # A Pokémon can have one or more types, so we must add its level to each corresponding type
            for pokemon_type in types:
                # If the type does not exist in the dictionary yet, create an empty list for that type
                if pokemon_type not in type_levels:
                    type_levels[pokemon_type] = []
                # Add the Pokémon's level to the list for this type
                type_levels[pokemon_type].append(level)

        # Display the average level for each Pokémon type
        for pokemon_type, levels in type_levels.items():
            # Calculate the average level for the current type
            average_level = sum(levels) / len(levels)
            # Print the results
            print(f"Tipo: {pokemon_type} → Promedio de nivel: {average_level:.1f}")
            

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