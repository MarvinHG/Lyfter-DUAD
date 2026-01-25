'''
2. Experimente con el concepto de scope:
    1. Intente accesar a una variable definida dentro de una función desde afuera.
    2. Intente accesar a una variable global desde una función y cambiar su valor.
'''

#1 Intente accesar a una variable definida dentro de una función desde afuera.
def local_variable_function():
    local_variable = 26
# print(local_variable) # -> NameError: name 'local_variable' is not defined.

#2 Intente accesar a una variable global desde una función y cambiar su valor.
counter = 0
def global_variable_function():
    global counter 
    counter +=1

global_variable_function()
global_variable_function()

print(counter)