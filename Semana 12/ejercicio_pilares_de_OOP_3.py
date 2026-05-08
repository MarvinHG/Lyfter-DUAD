'''
Ejercicios de Los 4 Pilares de OOP #3

Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.
'''

'''
# Explicacion

La herencia múltiple es un concepto de la programación orientada a objetos donde una clase puede 
heredar de más de una clase padre al mismo tiempo.
Esto permite que una clase combine atributos y métodos de varias clases, reutilizando código y agregando 
múltiples comportamientos.

'''

# Exaple 1
# Create class A with a method
class A:
    def metodo_a(self):
        print("Método A")

# Create class B with a method
class B:
    def metodo_b(self):
        print("Método B")

# Create class C that inherits from both A and B
class C(A, B):
    pass

# Example usage
objeto_c = C()
objeto_c.metodo_a()  # Show output: Método A
objeto_c.metodo_b()  # Show output: Método B


#Example 2
# Create class Flyable with a method
class Flyable:
    def fly(self):
        print("Estoy volando")

# Create class Swimmable with a method
class Swimmable:
    def swim(self):
        print("Estoy nadando")

# Create class Duck that inherits from both Flyable and Swimmable
class Duck(Flyable, Swimmable):
    def sound(self):
        print("Cuack")


# Example usage
duck = Duck()
duck.fly()
duck.swim()
duck.sound()