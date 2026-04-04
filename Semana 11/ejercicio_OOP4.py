'''
Ejercicio OOP #4
Cree las siguientes clases:
Head
Torso
Arm
Hand
Leg
Feet
Ahora cree una clase de Human y conecte todas las clases de manera lógica por medio de atributos.
'''
class Head:
    def __init__(self):
        pass

class Hand:
    def __init__(self):
        pass

class Feet:
    def __init__(self):
        pass

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Leg:
    def __init__(self, feet):
        self.feet = feet

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Human:
    def __init__(self):
        self.torso = Torso(Head(), Arm(Hand()), Arm(Hand()), Leg(Feet()), Leg(Feet()))

person = Human()

print(person.torso.head)
print(person.torso.right_arm.hand)