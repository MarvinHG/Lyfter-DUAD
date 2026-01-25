'''
2. Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.

(Considere que las palabras están separadas por espacios y/o saltos de línea)

- Ejemplo:
    - Salida: "Este archivo contiene " 123 "palabras"
'''
from pathlib import Path # Used to handle file paths in a clean and cross-platform way

# Function to read the file and count the words
def open_and_count_words(input_file):
    try:
        # Read the input file line by line 
        with open(input_file, 'r', encoding='utf-8') as file:
            #Save the file in a list
            lines = [line.strip() for line in file]

        # Transform the list into a single string separated by spaces
        one_line = " ".join(lines)

        #Count the words in the list
        words = len(one_line.split())
        return words

    except (FileNotFoundError, PermissionError):
        # Raise these Exception
        raise

    except Exception as e:
        # Wrap any unexpected exception with more context
        raise RuntimeError(
            f"Error procesando el archivo '{input_file}'"
        ) from e

# Main Function
def main():
    try:
        # Get the directory where the current script is located
        base_path = Path(__file__).parent
        # Build full paths for input and output files
        input_file = base_path / "Multi_lines.txt"

        # Call the function to process the files
        num = open_and_count_words(input_file)

        # Print the results
        print(f"Este archivo contiene {num} palabras")

    except FileNotFoundError:
        print("Error: el archivo Multi_lines.txt no existe.")

    except PermissionError:
        print("Error: permisos insuficientes.")

    except RuntimeError as e:
        print(f"{e}")

    except Exception as e:
        print(f"Error inesperado: {e}")



# Run the program only if it is executed directly
if __name__ == '__main__':
    main()