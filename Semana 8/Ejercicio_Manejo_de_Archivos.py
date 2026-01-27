'''
**Ejercicios**

1. Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados 
alfabéticamente.
'''
from pathlib import Path # Used to handle file paths in a clean and cross-platform way

# Function to read the file and create a new sorted one
def open_and_create_a_new_file(input_file, output_file):
    try:
        # Read the input file line by line
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file]

        # Sort the lines alphabetically (case-insensitive)
        lines.sort(key=str.lower)

        # Write the sorted content to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('\n'.join(lines))

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
        input_file = base_path / "Music.txt"
        output_file = base_path / "Sorted_Music.txt"

        # Call the function to process the files
        open_and_create_a_new_file(input_file, output_file)
        # Inform that the file was created successfully
        print("✅ Archivo creado correctamente: Sorted_Music.txt")

    except FileNotFoundError:
        print("Error: el archivo Music.txt no existe.")

    except PermissionError:
        print("Error: permisos insuficientes.")

    except RuntimeError as e:
        print(f"{e}")

    except Exception as e:
        print(f"Error inesperado: {e}")


# Run the program only if it is executed directly
if __name__ == '__main__':
    main()
