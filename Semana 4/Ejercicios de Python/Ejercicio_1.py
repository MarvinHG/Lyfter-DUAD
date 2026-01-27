'''
1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
    1. Si le salen errores, **no se asuste.** Lealos e intente comprender qué significan.
    *Los errores son oportunidades de aprendizaje.*
    2. Por ejemplo:
        1. string + string → ?
        2. string + int → ?
        3. int + string → ?
        4. list + list → ?
        5. string + list → ?
        6. float + int → ?
        7. bool + bool → ?
'''
# 1. string + string → ?
string1 = "Marvin"
string2 = "Hernandez"
# print(string1 + string2) ->MarvinHernandez

# 2. string + int → ?
string3 = "Gonzalez"
int1 = 28
# print(string3 + int1) -> TypeError: can only concatenate str (not "int") to str

# 3. int + string → ?
string4 = "Hola"
int2 = 5
# print(int2 + string4) -> TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 4. list + list → ?
list1 = [1 , 2 , 3]
list2 = [4 , 5 , 6]
# print(list1 + list2) -> [1, 2, 3, 4, 5, 6]

# 5. string + list → ?
string5 = "Hola Mundo"
list3 = ["a", "b", "c"]
# print(string5 + list3) -> TypeError: can only concatenate str (not "list") to str

# 6. float + int → ?
float1 = 3.14
int3 = 10
# print(float1 + int3) -> 13.14

# 7. bool + bool → ?
boolTrue = True
boolFalse = False
# print(boolTrue + boolFalse) -> 1 
# print(boolFalse + boolFalse) -> 0
# print(boolTrue + boolTrue) -> 2