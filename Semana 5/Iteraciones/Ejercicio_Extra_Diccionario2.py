'''
1. Agrupar empleados por departamento
- Dada una lista de empleados donde cada uno tiene nombre, correo y departamento, cree un diccionario que agrupe los empleados por su departamento:
- Ejemplo:
    - Entrada:
        
        ```python
        employees = [
            {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
            {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
            {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
            {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
        ]
        ```
'''
# List of employees
employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana",    "email": "ana@empresa.com",    "department": "TI"},
    {"name": "Luis",   "email": "luis@empresa.com",   "department": "Ventas"},
    {"name": "Sofía",  "email": "sofia@empresa.com",  "department": "RRHH"},
]
# Create an empty dictionary to store employees grouped by department
gropued_by_department = {}

# Loop through each employee in the list
for employee in employees:
    # Extract the department of the current employee
    department = employee["department"]

    # If the department is not yet in the dictionary, create a new empty list for it
    if department not in gropued_by_department:
        gropued_by_department[department] = []
    # Add the employee's name and email to the corresponding department list
    gropued_by_department[department].append({
    "name": employee["name"],
    "email": employee["email"]
})

# Print the final dictionary with employees grouped by department
print(gropued_by_department)