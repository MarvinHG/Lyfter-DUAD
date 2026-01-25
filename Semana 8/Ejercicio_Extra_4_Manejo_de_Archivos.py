'''
1. Cree un programa que:
- Pida al usuario una línea de texto
- Agregue esa línea **al final** de un archivo existente
- Si el archivo no existe, lo crea automáticamente
- Ejemplo:
    - Entrada:
        
        ```python
        "Este es un nuevo registro"
        ```
        
    - Salida:
        "El texto se agrega al final del archivo sin borrar lo anterior"
'''
from pathlib import Path # Used to handle file paths in a clean and cross-platform way

# Function to read a file and add new info
def open_and_add_info_to_file(input_file):
    # Requests the user's info
    info = input("Que informacion desea agregar al archivo: ")
    try:
        if input_file.exists():
            # If the file exists add the info
            with open(input_file, 'a', encoding='utf-8') as file:
                file.write(f"{info}\n")
                print("El texto se agrega al final del archivo sin borrar lo anterior")
        else:
            # If the file does not exist, create the file and add the info
            with open(input_file, 'w', encoding='utf-8') as file:
                file.write(f"{info}\n")
                print("Este es un nuevo registro")

    except PermissionError:
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
        input_file = base_path / "Add_info.txt"

        # Call the function to process the files
        open_and_add_info_to_file(input_file,)

    except PermissionError:
        print("Error: permisos insuficientes.")

    except RuntimeError as e:
        print(f"{e}")

    except Exception as e:
        print(f"Error inesperado: {e}")


# Run the program only if it is executed directly
if __name__ == '__main__':
    main()
