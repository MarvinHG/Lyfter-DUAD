'''
3. Cree un programa que:
- Lea un archivo línea por línea
- Convierta cada línea a **mayúsculas**
- Escriba el contenido en un **nuevo archivo**
- Ejemplo:
    - Entrada:
        
        ```python
        # archivo original:
        hola mundo
        esto es python
        ```
        
    - Salida:
        
        ```python
        # archivo nuevo:
        HOLA MUNDO
        ESTO ES PYTHON
        ```
        
'''
from pathlib import Path # Used to handle file paths in a clean and cross-platform way

# Function to read the file and create a new one with uppercase words
def open_and_create_a_new_file(input_file, output_file):
    try:
        # Read the input file line by line
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file]

        # Convert each line to uppercase
        upper_lines = [words.upper() for words in lines]

        # Write the uppercase content to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('\n'.join(upper_lines))

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
        input_file = base_path / "Lowercase.txt"
        output_file = base_path / "Uppercase.txt"

        # Call the function to process the files
        open_and_create_a_new_file(input_file, output_file)
        # Inform that the file was created successfully
        print("✅ Archivo creado correctamente: Uppercase.txt")

    except FileNotFoundError:
        print("Error: el archivo Lowercase.txt no existe.")

    except PermissionError:
        print("Error: permisos insuficientes.")

    except RuntimeError as e:
        print(f"{e}")

    except Exception as e:
        print(f"Error inesperado: {e}")


# Run the program only if it is executed directly
if __name__ == '__main__':
    main()
