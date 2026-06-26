'''
Ejercicios de Estructuras de Datos 2

Cree una estructura de objetos que asemeje un Double Ended Queue.
    Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio y al final) y 
    pop_left y pop_right (para quitar nodos al inicio y al final).
    Debe incluir un método para hacer print de toda la estructura.
    No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.
'''
class Node:
    # Represents a single element (node) in the Stack
    data: str

    def __init__(self, data, next=None):
        self.data = data # data: value stored in the node
        self.next = next # next: reference to the next node in the stack


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    #Method to Add a new node to the head(left) of the stack
    def push_left(self, data):
        new_node = Node(data)

        # If the deque is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # Connect new node to first node
        new_node.next = self.head
        # Move head pointer
        self.head = new_node
    
    #Method to Add a new node to the tail(right) of the stack
    def push_right(self, data):
        new_node = Node(data)

        # If the deque is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # Connect last node to new node
        self.tail.next = new_node

        # Move tail pointer
        self.tail = new_node

    #Method to Remove the head(left) node from the stack
    def pop_left(self):
        # Check if Deque is empty
        if self.head is None:
            print("El Deque está vacío")
            return

        # Move head pointer to the next node (removing current head)
        self.head = self.head.next

        # If the head is empty the tail should be empty
        if self.head is None:
            self.tail = None

    #Method to Remove the tail(right) node from the stack
    def pop_right(self):
        # Check if Deque is empty
        if self.head is None:
            print("El Deque está vacío")
            return
        
        # Case: only one node
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        current_node = self.head

        while current_node.next != self.tail:
            current_node = current_node.next

        # current_node is now the penultimate node
        current_node.next = None
        self.tail = current_node

    #Method to Print all elements in the stack from top to bottom
    def print_deque(self):
        current_node = self.head

        # If stack is empty, notify user
        if current_node is None:
            print("El Deque está vacío")
            return

        # Traverse the linked nodes until the end
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        

# -------------------------
# Testing the Deque
# -------------------------

deque = Deque()

print("== Adding elements to the RIGHT ==")
deque.push_right("A")
deque.push_right("B")
deque.push_right("C")

print("\n== Current Deque ==")
deque.print_deque()

print("\n== Adding element to the LEFT ==")
deque.push_left("X")

print("\n== Current Deque ==")
deque.print_deque()

print("\n== pop_left ==")
deque.pop_left()

print("\n== After pop_left ==")
deque.print_deque()

print("\n== pop_right ==")
deque.pop_right()

print("\n== Final Deque ==")
deque.print_deque()