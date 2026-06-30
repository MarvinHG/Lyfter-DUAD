'''
Ejercicios de Estructuras de Datos 1

Cree una estructura de objetos que asemeje un Stack.
    Debe incluir los métodos de push (para agregar nodos) y pop (para quitar nodos).
    Debe incluir un método para hacer print de toda la estructura.
    No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.
'''

class Node:
    # Represents a single element (node) in the Stack
    data: str

    def __init__(self, data, next=None):
        self.data = data # data: value stored in the node
        self.next = next # next: reference to the next node in the stack


class Stack:
    def __init__(self):
        # top points to the last inserted node (top of the stack)
        self.top = None 

    #Method to Add a new node to the top of the stack
    def push(self, new_node): 
        new_node.next = self.top # New node points to current top
        self.top = new_node # Update top to the new node
    
    #Method to Remove the top node from the stack
    def pop(self):
        # Check if stack is empty
        if self.top is None:
            print("El Stack está vacío")
            return

        # Move top pointer to the next node (removing current top)
        self.top = self.top.next
    

    #Method to Print all elements in the stack from top to bottom
    def print_stack(self):
        current_node = self.top

        # If stack is empty, notify user
        if current_node is None:
            print("El Stack está vacío")
            return

        # Traverse the linked nodes until the end
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


# -------------------------
# Testing the Stack
# -------------------------

stack = Stack()

print("== Agregando nodos ==")

stack.push(Node("A"))
stack.push(Node("B"))
stack.push(Node("C"))

print("\n== Stack actual ==")
stack.print_stack()

print("\n== Haciendo pop ==")
stack.pop()

print("\n== Stack después del pop ==")
stack.print_stack()

print("\n== Otro pop ==")
stack.pop()

print("\n== Stack final ==")
stack.print_stack()