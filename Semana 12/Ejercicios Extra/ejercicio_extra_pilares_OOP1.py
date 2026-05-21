'''
Ejercicios extra de Los 4 Pilares de OOP #1

Cree una clase Employee con los siguientes requisitos:
Atributos privados: _name, _salary
Use @property y @<atributo>.setter para:
Mostrar el nombre y el salario
Validar que el salario nunca sea negativo
Cree un método promote que aumente el salario un porcentaje definido
Ejemplo:
Entrada:
    employee = Employee("Ana",1000)

    employee.promote(0.1) # +10%

Salida:
    print(employee.salary) # 1100

'''
#Create the Employee class
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.salary = salary  

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    # Getter for salary
    @property
    def salary(self):
        return self._salary

    # Setter for salary with validation
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            print("El salario no puede ser negativo.")
        else:
            self._salary = new_salary

    # Method for increasing salary by a percentage
    def promote(self, percentage):
        self._salary += self._salary * percentage


# Example
employee = Employee("Ana", 1000)

employee.promote(0.1)  # 10% increase

print(employee.salary)  # 1100.0