'''
1. Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON ([Archivos JSON](https://www.notion.so/Archivos-JSON-79f9758cb59d4452a9c8668efa25356c?pvs=21)).
    1. Debe leer el archivo para importar los Pokémones existentes.
    2. Luego debe pedir la información del Pokémon a agregar.
    3. Finalmente debe guardar el nuevo Pokémon en el archivo.
'''
from pathlib import Path # Used to handle file paths in a clean and cross-platform way
import json              # Used to work with JSON files

# Function to read a JSON file and convert its content into a Python object
def read_json_file(file_path):
        # Open the JSON file in read mode with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            # Convert JSON data into a Python list of dictionaries
            pokemons = json.load(file)

        # Return the list of existing Pokémon
        return pokemons


# Function that asks the user for Pokémon data and returns it as a dictionary
def get_new_pokemon():
    # Ask for the Pokémon name
    name = input("Ingresa el nombre del nuevo Pokemon: ").strip()
    # Ask for the Pokémon type(s)
    pokemon_types = input(
        "Ingresa el tipo o los tipos del pokemon (separados por comas, ejemplo: Fuego, Agua): "
    ).strip()

    # Convert the string of types into a list and remove extra spaces
    types = [t.strip() for t in pokemon_types.split(",")]

    print("\nIngresa los stats base del Pokemon:")
    # Keep asking for stats until valid numeric values are entered
    while True:
        try:
            hp = int(input("HP: "))
            attack = int(input("Attack: "))
            defense = int(input("Defense: "))
            sp_attack = int(input("Sp. Attack: "))
            sp_defense = int(input("Sp. Defense: "))
            speed = int(input("Speed: "))
            break  # Exit the loop if all values are valid
        except ValueError:
            # Handle invalid numeric input
            print("Por favor ingresa SOLO números. Intenta de nuevo.\n")

    # Create the Pokémon dictionary following the JSON structure
    new_pokemon = {
        "name": {
            "english": name
        },
        "type": types,
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }

    # Return the new Pokémon dictionary
    return new_pokemon


# Function to add a new Pokémon to the existing Pokémon list
def add_new_pokemon(pokemon_dictionary, new_pokemon):
    # Append the new Pokémon to the list
    pokemon_dictionary.append(new_pokemon)
    # Return the new Pokémon dictionary with the new pokemon
    return pokemon_dictionary


# Function to save the updated Pokémon list back into the JSON file
def convert_to_json(file_path, pokemons):
    # Open the JSON file in write mode
    with open(file_path, 'w', encoding='utf-8') as file:
        # Write the Python object into the JSON file with proper formatting
        json.dump(pokemons, file, ensure_ascii=False, indent=4)

    print("\nPokémon agregado correctamente!")


# Main function that controls the program flow
def main():
    base_path = Path(__file__).parent # Gets the directory where the script is located
    file_name = base_path / "pokemon.json" # Builds the full path to the CSV file
    
    # Read existing Pokémon from the JSON file
    pokemon_dictionary = read_json_file(file_name)
    # Get new Pokémon data from the user
    new_pokemon = get_new_pokemon()
    # Add the new Pokémon to the list
    pokemons = add_new_pokemon(pokemon_dictionary, new_pokemon)
    # Save the updated list back to the JSON file
    convert_to_json(file_name, pokemons)

# Program entry point
if __name__ == "__main__":
    main()