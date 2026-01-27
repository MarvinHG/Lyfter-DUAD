'''
1. Cree un programa que lea un archivo con texto línea por línea, quite los saltos de línea (\n) 
y escriba todo el contenido en un **solo renglón** en un nuevo archivo - Ejemplo: - Entrada:
python
        Hola
        mundo
        esto
        es
        Python
- Salida:
python
        "Hola mundo esto es Python"
'''
from pathlib import Path # Used to handle file paths in a clean and cross-platform way

# Function to read a file and write its content into a single line
def open_and_create_a_new_file(input_file, output_file):
    try:
        # Read the input file line by line 
        with open(input_file, 'r', encoding='utf-8') as file:
            #Save the file in a list
            lines = [line.strip() for line in file]

        #Transfor the list into a string, and separate them with with spaces
        one_line = " ".join(lines)

        #Write the content to the output file in one line
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(one_line)

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
        output_file = base_path / "One_line.txt"

        # Call the function to process the files
        open_and_create_a_new_file(input_file, output_file)
        # Inform that the file was created successfully
        print("✅ Archivo creado correctamente: One_line.txt")

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