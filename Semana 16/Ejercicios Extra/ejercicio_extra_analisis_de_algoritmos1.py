'''
Ejercicios Extra de Análisis de Algoritmos #1

Los siguientes dos algoritmos hacen lo mismo: calcular la suma de los primeros n números naturales
- Versión 1:
    def manual_add(n):
        result = 0
        for i in range(1, number + 1):
            result += i
        return result

- Versión 2:
    def add_formula(n):
        return number * (number + 1) // 2


Preguntas:
¿Cuál es la complejidad de cada versión?
¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?

'''

def manual_add(n):
    result = 0  # O(1)
    for i in range(1, n + 1):  # O(n)
        result += i  # O(1)
    return result  # O(1)


def add_formula(n):
    return n * (n + 1) // 2  # O(1)


# Test version 1
print("Versión 1:", manual_add(10))

# Test version 2
print("Versión 2:", add_formula(10))

'''
Preguntas:
¿Cuál es la complejidad de cada versión?
La version 1 es O(n)
La version 2 es O(1)
¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?
Usaria la version 2, porque la primera versión tendría que realizar mil millones de iteraciones, 
mientras que la segunda obtiene el resultado con una formula
'''